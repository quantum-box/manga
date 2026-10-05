import Foundation

struct MangaTitle: Identifiable, Hashable, Codable {
    let id: String
    let title: String
    let genre: String
    let image: String
    let tagline: String
    let synopsis: String
    let episodes: [Episode]
    var revision: String? = nil
    var episodeCount: Int { Set(episodes.map(\.number)).count }
    var orderedEpisodes: [Episode] {
        episodes.enumerated().sorted { a, b in
            a.element.number == b.element.number ? a.offset < b.offset : a.element.number < b.element.number
        }.map(\.element)
    }
    var primaryEpisodes: [Episode] {
        var seen = Set<Int>()
        return orderedEpisodes.filter { seen.insert($0.number).inserted }
    }
    func otherEditions(of episode: Episode) -> [Episode] {
        orderedEpisodes.filter { $0.number == episode.number && $0.id != episode.id }
    }
}

struct Episode: Identifiable, Hashable, Codable {
    let id: String
    let number: Int
    let title: String
    let edition: String
    let reader: String
    let background: String
    var revision: String? = nil
}

enum Catalog {
    enum LoadError: Error {
        case missingCatalog, emptyCatalog
    }

    static var apiBaseURL: URL {
        URL(string: Bundle.main.object(forInfoDictionaryKey: "MangaAPIBaseURL") as? String
            ?? "https://manga-server.txcloud.app")!
    }

    static var remoteCacheURL: URL { OfflineDownloads.root.appendingPathComponent(".online-catalog.json") }
    static func cachedRemote(cacheURL: URL = remoteCacheURL) -> [MangaTitle]? {
        guard let data = try? Data(contentsOf: cacheURL), let titles = try? validatedRemote(data) else { return nil }
        return titles
    }
    private static func validatedRemote(_ data: Data) throws -> [MangaTitle] {
        let titles = try JSONDecoder().decode([MangaTitle].self, from: data)
        guard titles.allSatisfy({ title in
            remoteURL(title.image) != nil && title.episodes.allSatisfy { remoteURL($0.reader) != nil }
        }) else { throw URLError(.unsupportedURL) }
        return titles.map { title in
            MangaTitle(id: title.id, title: title.title, genre: title.genre, image: title.image, tagline: title.tagline,
                       synopsis: title.synopsis, episodes: title.orderedEpisodes, revision: title.revision)
        }
    }
    static func loadRemote(session: URLSession = .shared, cacheURL: URL? = nil) async throws -> [MangaTitle] {
        var request = URLRequest(url: apiBaseURL.appendingPathComponent("api/v1/catalog"))
        request.timeoutInterval = 20
        request.cachePolicy = .useProtocolCachePolicy
        let (data, response) = try await session.data(for: request)
        guard let response = response as? HTTPURLResponse, response.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
        let titles = try validatedRemote(data)
        if let cacheURL {
            try? FileManager.default.createDirectory(at: cacheURL.deletingLastPathComponent(), withIntermediateDirectories: true)
            try? JSONEncoder().encode(titles).write(to: cacheURL, options: .atomic)
        }
        return titles
    }

    // API paths are relative to the configured HTTPS origin; external URLs are rejected.
    static func remoteURL(_ path: String) -> URL? {
        guard apiBaseURL.scheme == "https", path.hasPrefix("/"), !path.hasPrefix("//"),
              let url = URL(string: path, relativeTo: apiBaseURL)?.absoluteURL,
              url.host == apiBaseURL.host, url.scheme == "https", url.user == nil else { return nil }
        return url
    }

    static func readerURL(_ path: String) -> URL? {
        path.hasPrefix("/") ? remoteURL(path) : resource(path)
    }

    static func load(resourceURL: URL? = Bundle.main.resourceURL) throws -> [MangaTitle] {
        guard let url = resource("catalog.json", resourceURL: resourceURL) else {
            throw LoadError.missingCatalog
        }
        let titles = try JSONDecoder().decode([MangaTitle].self, from: Data(contentsOf: url))
        guard !titles.isEmpty else { throw LoadError.emptyCatalog }
        return titles
    }

    static func loadOffline() throws -> [MangaTitle] {
        let saved = try OfflineDownloads.load()
        return saved + (try load()).filter { title in !saved.contains { $0.id == title.id } }
    }

    static func resource(_ path: String, resourceURL: URL? = Bundle.main.resourceURL) -> URL? {
        if path.hasPrefix("downloads/") {
            return OfflineDownloads.resource(String(path.dropFirst("downloads/".count)))
        }
        guard let root = resourceURL?.appendingPathComponent("Webtoons", isDirectory: true)
            .resolvingSymlinksInPath().standardizedFileURL else { return nil }
        // iPhone app bundles use /private/var; Foundation can resolve it to /var.
        // Compare two canonical paths so a bundled file is not rejected as outside the folder.
        let url = root.appendingPathComponent(path).resolvingSymlinksInPath().standardizedFileURL
        guard url.path.hasPrefix(root.path + "/"), FileManager.default.fileExists(atPath: url.path) else { return nil }
        return url
    }
}

// Completed downloads live in Application Support, not the evictable URL cache.
enum OfflineDownloads {
    static var root: URL {
        FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("MangaDownloads", isDirectory: true)
    }
    static func resource(_ path: String) -> URL? {
        let base = root.resolvingSymlinksInPath().standardizedFileURL
        let url = base.appendingPathComponent(path).resolvingSymlinksInPath().standardizedFileURL
        guard url.path.hasPrefix(base.path + "/"), FileManager.default.fileExists(atPath: url.path) else { return nil }
        return url
    }
    static func load(root: URL = root) throws -> [MangaTitle] {
        guard FileManager.default.fileExists(atPath: root.path) else { return [] }
        return try FileManager.default.contentsOfDirectory(at: root, includingPropertiesForKeys: nil)
            .filter { !$0.lastPathComponent.hasPrefix(".") }
            .compactMap { try? JSONDecoder().decode(MangaTitle.self, from: Data(contentsOf: $0.appendingPathComponent("title.json"))) }
            .sorted { $0.title < $1.title }
    }
    static func isSaved(_ title: MangaTitle) -> Bool {
        guard let saved = ((try? load()) ?? []).first(where: { $0.id == title.id }) else { return false }
        return title.primaryEpisodes.allSatisfy { episode in saved.episodes.contains { $0.id == episode.id && $0.revision == episode.revision } }
    }
}

actor DownloadManager {
    static let shared = DownloadManager()
    private var active = Set<String>()
    private var revisions = [String: Int]()
    enum DownloadError: Error { case invalidContent, tooLarge, alreadyDownloading }
    private func safe(_ value: String) -> Bool {
        !value.isEmpty && value.count <= 80 && value.utf8.allSatisfy { (48...57).contains($0) || (65...90).contains($0) || (97...122).contains($0) || $0 == 45 || $0 == 95 }
    }
    private func escape(_ text: String) -> String {
        text.replacingOccurrences(of: "&", with: "&amp;").replacingOccurrences(of: "<", with: "&lt;")
            .replacingOccurrences(of: ">", with: "&gt;").replacingOccurrences(of: "\"", with: "&quot;")
    }
    func delete(_ titleID: String, root: URL = OfflineDownloads.root) throws {
        revisions[titleID, default: 0] += 1
        guard FileManager.default.fileExists(atPath: root.path) else { return }
        for folder in try FileManager.default.contentsOfDirectory(at: root, includingPropertiesForKeys: nil) {
            guard !folder.lastPathComponent.hasPrefix("."),
                  let data = try? Data(contentsOf: folder.appendingPathComponent("title.json")),
                  let title = try? JSONDecoder().decode(MangaTitle.self, from: data), title.id == titleID else { continue }
            try FileManager.default.removeItem(at: folder)
        }
    }

    func download(_ title: MangaTitle, episodeIDs: Set<String>? = nil, root: URL = OfflineDownloads.root, session: URLSession = .shared,
                  progress: (Int, Int) async -> Void = { _, _ in }) async throws {
        let existing = try OfflineDownloads.load(root: root).first { $0.id == title.id }
        let requested = title.orderedEpisodes.filter { episodeIDs == nil || episodeIDs!.contains($0.id) }
        guard !requested.isEmpty else { throw DownloadError.invalidContent }
        if let revision = title.revision, existing?.revision == revision,
           requested.allSatisfy({ requested in existing?.episodes.contains { $0.id == requested.id && $0.revision == requested.revision } == true }) { return }
        guard active.insert(title.id).inserted else { throw DownloadError.alreadyDownloading }
        defer { active.remove(title.id) }
        let revision = revisions[title.id, default: 0]
        let manager = FileManager.default
        try manager.createDirectory(at: root, withIntermediateDirectories: true)
        // Exclude re-downloadable comics from iCloud backup; Application Support retains them offline.
        var directory = root
        var values = URLResourceValues(); values.isExcludedFromBackup = true
        try directory.setResourceValues(values)
        let existingFolder = existing?.image.split(separator: "/").dropFirst().first.map(String.init)
        let folder = existingFolder ?? UUID().uuidString
        guard safe(folder) else { throw DownloadError.invalidContent }
        let staging = root.appendingPathComponent("." + UUID().uuidString, isDirectory: true)
        try manager.createDirectory(at: staging, withIntermediateDirectories: true)
        defer { try? manager.removeItem(at: staging) }
        var totalBytes = 0
        func get(_ path: String, limit: Int, expectedRevision: String? = nil) async throws -> Data {
            try Task.checkCancellation()
            guard let url = Catalog.remoteURL(path) else { throw DownloadError.invalidContent }
            var request = URLRequest(url: url); request.timeoutInterval = 60
            let (data, response) = try await session.data(for: request)
            guard let http = response as? HTTPURLResponse, http.statusCode == 200 else { throw URLError(.badServerResponse) }
            if let expectedRevision {
                guard var etag = http.value(forHTTPHeaderField: "ETag") else { throw DownloadError.invalidContent }
                // Cloudflare compression changes strong ETags to W/"..." without changing the content revision.
                if etag.hasPrefix("W/") { etag.removeFirst(2) }
                guard etag.trimmingCharacters(in: CharacterSet(charactersIn: "\"")) == expectedRevision else { throw DownloadError.invalidContent }
            }
            // Redirects must remain on the configured server.
            guard response.url?.host == Catalog.apiBaseURL.host, response.url?.scheme == "https" else { throw DownloadError.invalidContent }
            totalBytes += data.count
            guard data.count <= limit, totalBytes <= 256 * 1024 * 1024 else { throw DownloadError.tooLarge }
            return data
        }
        let cover = try await get(title.image, limit: 16 * 1024 * 1024)
        try cover.write(to: staging.appendingPathComponent("cover"), options: .atomic)
        var episodes = [Episode]()
        if episodeIDs != nil, let existing {
            for savedEpisode in existing.episodes where !requested.contains(where: { $0.id == savedEpisode.id }) {
                guard safe(savedEpisode.id),
                      title.episodes.contains(where: { $0.id == savedEpisode.id && $0.revision == savedEpisode.revision }),
                      let existingFolder else { continue }
                let source = root.appendingPathComponent(existingFolder).appendingPathComponent(savedEpisode.id)
                if manager.fileExists(atPath: source.path) {
                    try manager.copyItem(at: source, to: staging.appendingPathComponent(savedEpisode.id))
                    episodes.append(savedEpisode)
                }
            }
        }
        for (index, episode) in requested.enumerated() {
            guard safe(episode.id) else { throw DownloadError.invalidContent }
            let data = try await get("/api/episodes/" + episode.id, limit: 256 * 1024, expectedRevision: episode.revision ?? title.revision)
            guard let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
                  let blocks = json["blocks"] as? [[String: Any]], !blocks.isEmpty else { throw DownloadError.invalidContent }
            let episodeDir = staging.appendingPathComponent(episode.id, isDirectory: true)
            try manager.createDirectory(at: episodeDir, withIntermediateDirectories: true)
            var body = "<h1>" + escape(episode.title) + "</h1>"
            if let subtitle = json["subtitle"] as? String { body += "<p>" + escape(subtitle) + "</p>" }
            for block in blocks {
                switch block["type"] as? String {
                case "image":
                    guard let src = block["src"] as? String, let dot = src.lastIndex(of: "."),
                          safe(String(src[..<dot])), ["png", "jpg", "webp"].contains(String(src[src.index(after: dot)...])) else { throw DownloadError.invalidContent }
                    let bytes = try await get("/images/" + episode.id + "/" + src, limit: 16 * 1024 * 1024)
                    try bytes.write(to: episodeDir.appendingPathComponent(src), options: .atomic)
                    body += "<img src=\"" + src + "\" alt=\"" + escape(block["alt"] as? String ?? "") + "\">"
                case "spacer": body += "<div class=\"spacer " + ((block["size"] as? String == "long") ? "long" : "") + "\"></div>"
                case "caption", "ending", "speech":
                    let text = (block["type"] as? String == "speech") ? (block["speaker"] as? String ?? "") + "「" + (block["text"] as? String ?? "") + "」" : (block["text"] as? String ?? "")
                    body += "<p>" + escape(text) + "</p>"
                default: throw DownloadError.invalidContent
                }
            }
            let html = """
            <!doctype html><html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
            <meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src 'self'; style-src 'unsafe-inline'">
            <style>body{margin:0;background:#111;color:#eee;font-family:system-ui}main{max-width:720px;margin:auto;padding-bottom:100px}img{display:block;width:100%}h1,p{padding:24px;line-height:1.8}.spacer{height:100px}.long{height:260px}</style><main>\(body)</main></html>
            """
            try Data(html.utf8).write(to: episodeDir.appendingPathComponent("index.html"), options: .atomic)
            episodes.append(Episode(id: episode.id, number: episode.number, title: episode.title, edition: episode.edition,
                reader: "downloads/\(folder)/\(episode.id)/index.html", background: "#111111", revision: episode.revision))
            await progress(index + 1, requested.count)
        }
        var saved = MangaTitle(id: title.id, title: title.title, genre: title.genre, image: "downloads/\(folder)/cover",
                              tagline: title.tagline, synopsis: title.synopsis, episodes: title.orderedEpisodes.compactMap { canonical in episodes.first { $0.id == canonical.id } })
        saved.revision = title.revision
        try JSONEncoder().encode(saved).write(to: staging.appendingPathComponent("title.json"), options: .atomic)
        try Task.checkCancellation()
        guard revisions[title.id, default: 0] == revision else { throw CancellationError() }
        let destination = root.appendingPathComponent(folder)
        if manager.fileExists(atPath: destination.path) {
            _ = try manager.replaceItemAt(destination, withItemAt: staging)
        } else { try manager.moveItem(at: staging, to: destination) }
    }
}

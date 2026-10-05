import Foundation
final class OfflineAPI: URLProtocol {
    static var failImage = false
    static var revision = "v1"
    static var weakETag = true
    static var paths = [String]()
    static var requests = 0
    static var episodeRevisions = [String: String]()
    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
        Self.requests += 1
        let path = request.url!.path
        Self.paths.append(path)
        let status = Self.failImage && path.hasSuffix("01.png") ? 503 : 200
        let data = path.hasPrefix("/api/episodes/") ? Data("""
        {"title":"Test","subtitle":"Subtitle","blocks":[{"type":"caption","text":"<script>bad()</script>"},{"type":"image","src":"01.png","alt":"test"}]}
        """.utf8) : Data([137, 80, 78, 71, 13, 10, 26, 10])
        client?.urlProtocol(self, didReceive: HTTPURLResponse(url: request.url!, statusCode: status, httpVersion: nil, headerFields: ["ETag": (Self.weakETag ? "W/" : "") + "\"" + (Self.episodeRevisions[path] ?? Self.revision) + "\""])!, cacheStoragePolicy: .notAllowed)
        client?.urlProtocol(self, didLoad: data)
        client?.urlProtocolDidFinishLoading(self)
    }
    override func stopLoading() {}
}
@main struct OfflineTests {
    static func main() async throws {
        let root = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        defer { try? FileManager.default.removeItem(at: root) }
        let config = URLSessionConfiguration.ephemeral; config.protocolClasses = [OfflineAPI.self]
        let session = URLSession(configuration: config)
        let episode = Episode(id: "test", number: 1, title: "Test", edition: "", reader: "/?episode=test", background: "#111111")
        var title = MangaTitle(id: "online-test", title: "Test", genre: "Webtoon", image: "/images/test/cover.png", tagline: "", synopsis: "", episodes: [episode])
        title.revision = "v1"
        OfflineAPI.failImage = true
        do { try await DownloadManager.shared.download(title, root: root, session: session); fatalError("Incomplete download accepted") } catch {}
        let incomplete = try OfflineDownloads.load(root: root)
        precondition(incomplete.isEmpty)
        OfflineAPI.failImage = false
        try await DownloadManager.shared.download(title, root: root, session: session)

        // Load only the persisted files with networking disabled.
        let titles = try OfflineDownloads.load(root: root)
        precondition(titles.count == 1)
        let reader = root.appendingPathComponent(String(titles[0].episodes[0].reader.dropFirst("downloads/".count)))
        let html = try String(contentsOf: reader, encoding: .utf8)
        precondition(html.contains("&lt;script&gt;") && !html.contains("<script>"))
        precondition(!html.contains("https://") && !html.contains("fetch("))
        precondition(FileManager.default.fileExists(atPath: reader.deletingLastPathComponent().appendingPathComponent("01.png").path))
        let count = OfflineAPI.requests
        try await DownloadManager.shared.download(title, root: root, session: session)
        precondition(count == OfflineAPI.requests)
        title.revision = "v2"
        OfflineAPI.revision = "wrong-revision"
        do { try await DownloadManager.shared.download(title, root: root, session: session); fatalError("Mismatched revision accepted") } catch {}
        OfflineAPI.revision = "v2"
        OfflineAPI.failImage = true
        do { try await DownloadManager.shared.download(title, root: root, session: session); fatalError("Failed update accepted") } catch {}
        let kept = try OfflineDownloads.load(root: root)
        precondition(kept[0].revision == "v1")
        OfflineAPI.failImage = false
        try await DownloadManager.shared.download(title, root: root, session: session)
        let updated = try OfflineDownloads.load(root: root)
        precondition(updated.count == 1 && updated[0].revision == "v2")
        precondition(try! String(contentsOf: reader, encoding: .utf8).contains("Subtitle"))
        session.invalidateAndCancel()
        try await DownloadManager.shared.delete(title.id, root: root)
        let deleted = try OfflineDownloads.load(root: root)
        precondition(deleted.isEmpty && !FileManager.default.fileExists(atPath: reader.path))
        let nextSession = URLSession(configuration: config)
        do {
            try await DownloadManager.shared.download(title, root: root, session: nextSession) { _, _ in
                try? await DownloadManager.shared.delete(title.id, root: root)
            }
            fatalError("Deleted download reappeared")
        } catch is CancellationError {}
        let afterRace = try OfflineDownloads.load(root: root)
        precondition(afterRace.isEmpty)
        let first = Episode(id: "first", number: 1, title: "First", edition: "", reader: "/?episode=first", background: "#111111", revision: "chapter-one")
        let second = Episode(id: "second", number: 2, title: "Second", edition: "", reader: "/?episode=second", background: "#111111", revision: "chapter-two")
        let series = MangaTitle(id: "online-series", title: "Series", genre: "Webtoon", image: "/images/first/cover.png", tagline: "", synopsis: "", episodes: [first, second], revision: "chapter-one:chapter-two")
        OfflineAPI.episodeRevisions = ["/api/episodes/first": "chapter-one", "/api/episodes/second": "chapter-two"]
        try await DownloadManager.shared.download(series, root: root, session: nextSession)
        let grouped = try OfflineDownloads.load(root: root)
        precondition(grouped.count == 1 && grouped[0].episodes.count == 2)
        precondition(grouped[0].episodes.map(\.revision) == ["chapter-one", "chapter-two"])
        try await DownloadManager.shared.delete(series.id, root: root)
        OfflineAPI.paths = []
        try await DownloadManager.shared.download(series, episodeIDs: ["first"], root: root, session: nextSession)
        precondition(OfflineAPI.paths.filter { $0.hasPrefix("/api/episodes/") } == ["/api/episodes/first"])
        let partial = try OfflineDownloads.load(root: root)
        precondition(partial.first!.episodes.count == 1)
        OfflineAPI.paths = []
        try await DownloadManager.shared.download(series, episodeIDs: ["second"], root: root, session: nextSession)
        precondition(OfflineAPI.paths.filter { $0.hasPrefix("/api/episodes/") } == ["/api/episodes/second"])
        let accumulated = try OfflineDownloads.load(root: root)
        precondition(accumulated[0].episodes.map(\.id) == ["first", "second"])
        print("PASS: reading one chapter downloads only it; later chapters retain earlier saved files")
        print("PASS: a grouped series verifies each chapter against its own revision")
        print("PASS: deletion removes files and prevents an in-flight download from restoring them")
        print("PASS: failed downloads stay hidden; completed files read without networking; duplicates reuse saved data")
    }
}

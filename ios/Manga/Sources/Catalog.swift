import Foundation

struct MangaTitle: Identifiable, Hashable, Decodable {
    let id: String
    let title: String
    let genre: String
    let image: String
    let tagline: String
    let synopsis: String
    let episodes: [Episode]
    var episodeCount: Int { Set(episodes.map(\.number)).count }
}

struct Episode: Identifiable, Hashable, Decodable {
    let id: String
    let number: Int
    let title: String
    let edition: String
    let reader: String
    let background: String
}

enum Catalog {
    enum LoadError: Error {
        case missingCatalog, emptyCatalog
    }

    static func load(resourceURL: URL? = Bundle.main.resourceURL) throws -> [MangaTitle] {
        guard let url = resource("catalog.json", resourceURL: resourceURL) else {
            throw LoadError.missingCatalog
        }
        let titles = try JSONDecoder().decode([MangaTitle].self, from: Data(contentsOf: url))
        guard !titles.isEmpty else { throw LoadError.emptyCatalog }
        return titles
    }

    static func resource(_ path: String, resourceURL: URL? = Bundle.main.resourceURL) -> URL? {
        guard let root = resourceURL?.appendingPathComponent("Webtoons", isDirectory: true)
            .resolvingSymlinksInPath().standardizedFileURL else { return nil }
        // iPhone app bundles use /private/var; Foundation can resolve it to /var.
        // Compare two canonical paths so a bundled file is not rejected as outside the folder.
        let url = root.appendingPathComponent(path).resolvingSymlinksInPath().standardizedFileURL
        guard url.path.hasPrefix(root.path + "/"), FileManager.default.fileExists(atPath: url.path) else { return nil }
        return url
    }
}

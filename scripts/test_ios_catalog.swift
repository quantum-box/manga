import Foundation

@main
struct CatalogTests {
    static func require(_ condition: @autoclosure () -> Bool, _ message: String) throws {
        if !condition() { throw NSError(domain: "CatalogTests", code: 1, userInfo: [NSLocalizedDescriptionKey: message]) }
    }

    static func main() throws {
        let manager = FileManager.default
        // Use a real /private/var alias, as on a device. A nonexistent path does not reproduce the bug.
        let temporary = URL(fileURLWithPath: "/private/var/tmp", isDirectory: true)
            .appendingPathComponent("manga-catalog-test-\(UUID().uuidString)", isDirectory: true)
        let app = temporary.appendingPathComponent("Manga.app", isDirectory: true)
        let webtoons = app.appendingPathComponent("Webtoons", isDirectory: true)
        try manager.createDirectory(at: webtoons.appendingPathComponent("story"), withIntermediateDirectories: true)
        defer { try? manager.removeItem(at: temporary) }

        let repository = URL(fileURLWithPath: manager.currentDirectoryPath, isDirectory: true)
        let bundled = CommandLine.arguments.dropFirst().first.map {
            URL(fileURLWithPath: $0, isDirectory: true)
        } ?? repository.appendingPathComponent("ios/Manga", isDirectory: true)
        let data = try Data(contentsOf: bundled.appendingPathComponent("Webtoons/catalog.json"))
        let expectedIDs = Set((try JSONSerialization.jsonObject(with: data) as? [[String: Any]] ?? [])
            .compactMap { $0["id"] as? String })
        try require(!expectedIDs.isEmpty, "Bundled fixture must contain title identifiers")
        let catalogURL = webtoons.appendingPathComponent("catalog.json")
        try data.write(to: catalogURL)
        try Data("reader".utf8).write(to: webtoons.appendingPathComponent("story/index.html"))
        try Data([0]).write(to: webtoons.appendingPathComponent("story/cover.png"))

        let oldRoot = app.appendingPathComponent("Webtoons", isDirectory: true)
        let oldFile = oldRoot.appendingPathComponent("catalog.json").standardizedFileURL
        try require(!oldFile.path.hasPrefix(oldRoot.path + "/"), "Fixture must reproduce the original device path rejection")
        for root in [app, app.standardizedFileURL] {
            let titles = try Catalog.load(resourceURL: root)
            try require(Set(titles.map(\.id)) == expectedIDs && titles.count == expectedIDs.count,
                        "Device path aliases must load every title from the bundled catalog")
            try require(titles.first(where: { $0.id == "swordsaint" })?.episodeCount == 10,
                        "Swordsaint must have ten distinct chapters regardless of catalog order")
            try require(Catalog.resource("story/index.html", resourceURL: root) != nil, "Reader must resolve")
            try require(Catalog.resource("story/cover.png", resourceURL: root) != nil, "Cover must resolve")
        }
        print("PASS: reproduced old rejection; both device path aliases load catalog, reader, and cover")

        let outside = temporary.appendingPathComponent("outside.html")
        try Data("outside".utf8).write(to: outside)
        try manager.createSymbolicLink(at: webtoons.appendingPathComponent("escape.html"), withDestinationURL: outside)
        try require(Catalog.resource("../../outside.html", resourceURL: app) == nil, "Traversal must remain rejected")
        try require(Catalog.resource("escape.html", resourceURL: app) == nil, "Symlink outside Webtoons must remain rejected")
        try require(Catalog.resource("absent.html", resourceURL: app) == nil, "Missing resources must remain rejected")
        print("PASS: missing resources and paths outside Webtoons are rejected")

        for contents in ["not json", "[]"] {
            try Data(contents.utf8).write(to: catalogURL)
            var failed = false
            do { _ = try Catalog.load(resourceURL: app) } catch { failed = true }
            try require(failed, "Invalid or empty catalog must report a load failure")
        }
        try manager.removeItem(at: catalogURL)
        var missingFailed = false
        do { _ = try Catalog.load(resourceURL: app) } catch { missingFailed = true }
        try require(missingFailed, "Missing catalog must report a load failure")
        print("PASS: missing, malformed, and empty catalogs are failures, not empty search results")

        let titles = try Catalog.load(resourceURL: bundled)
        let zeroBreak = titles.first { $0.id == "zero-break" }!
        let first = Catalog.resource(zeroBreak.episodes[0].reader, resourceURL: bundled)!
        let forward = URL(string: "../episode-02/index.html", relativeTo: first)!.absoluteURL
        let second = zeroBreak.linkedEpisode(to: forward, resourceURL: bundled)
        try require(second?.number == 2, "Embedded next link must select native chapter two")
        let backward = URL(string: "../episode-01/index.html", relativeTo: forward)!.absoluteURL
        try require(zeroBreak.linkedEpisode(to: backward, resourceURL: bundled)?.number == 1,
                    "Embedded previous link must select native chapter one")
        try require(zeroBreak.linkedEpisode(to: outside, resourceURL: bundled) == nil,
                    "Unknown file links must not change the native chapter")
        try require(zeroBreak.linkedEpisode(to: URL(string: "https://example.com")!, resourceURL: bundled) == nil,
                    "External links must not change the native chapter")
        print("PASS: bundled forward and backward links select native chapters; unknown links are rejected")
        let tower = titles.first { $0.id == "tower-forge" }!
        let towerList = bundled.appendingPathComponent("Webtoons/tower-forge/chapters.html")
        try require(!manager.fileExists(atPath: towerList.path), "The native list must work without bundled HTML")
        for episode in tower.episodes {
            let reader = Catalog.resource(episode.reader, resourceURL: bundled)!
            let html = try String(contentsOf: reader, encoding: .utf8)
            try require(html.contains("href=\"../chapters.html\""), "Fixture must exercise the actual list link")
            let list = URL(string: "../chapters.html", relativeTo: reader)!.absoluteURL
            for root in [bundled, bundled.standardizedFileURL] {
                try require(tower.linksToChapterList(to: list, resourceURL: root),
                            "Every bundled chapter list link must return to the native title list")
            }
            try require(!tower.linksToChapterList(to: reader, resourceURL: bundled), "Episode links must remain separate")
        }
        for rejected in [outside, URL(string: "https://example.com/chapters.html")!,
                         first.deletingLastPathComponent().deletingLastPathComponent().appendingPathComponent("chapters.html"),
                         towerList.deletingLastPathComponent().appendingPathComponent("absent.html")] {
            try require(!tower.linksToChapterList(to: rejected, resourceURL: bundled),
                        "External, other-title and unknown links must not close the reader")
        }
        print("PASS: all Tower Forge list links route natively without list HTML; unrelated links are rejected")
        for title in titles {
            try require(Catalog.resource(title.image, resourceURL: bundled) != nil, "Missing bundled cover: \(title.id)")
            for episode in title.episodes {
                try require(Catalog.resource(episode.reader, resourceURL: bundled) != nil, "Missing bundled reader: \(episode.id)")
            }
        }
        let readerCount = titles.reduce(0) { $0 + $1.episodes.count }
        print("PASS: bundle contains all \(titles.count) covers and all \(readerCount) readers")
    }
}

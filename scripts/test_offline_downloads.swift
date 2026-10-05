import Foundation
final class OfflineAPI: URLProtocol {
    static var failImage = false
    static var requests = 0
    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
        Self.requests += 1
        let path = request.url!.path
        let status = Self.failImage && path.hasSuffix("01.png") ? 503 : 200
        let data = path.hasPrefix("/api/episodes/") ? Data("""
        {"title":"Test","blocks":[{"type":"caption","text":"<script>bad()</script>"},{"type":"image","src":"01.png","alt":"test"}]}
        """.utf8) : Data([137, 80, 78, 71, 13, 10, 26, 10])
        client?.urlProtocol(self, didReceive: HTTPURLResponse(url: request.url!, statusCode: status, httpVersion: nil, headerFields: nil)!, cacheStoragePolicy: .notAllowed)
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
        let title = MangaTitle(id: "online-test", title: "Test", genre: "Webtoon", image: "/images/test/cover.png", tagline: "", synopsis: "", episodes: [episode])
        OfflineAPI.failImage = true
        do { try await DownloadManager.shared.download(title, root: root, session: session); fatalError("Incomplete download accepted") } catch {}
        let incomplete = try OfflineDownloads.load(root: root)
        precondition(incomplete.isEmpty)
        OfflineAPI.failImage = false
        try await DownloadManager.shared.download(title, root: root, session: session)
        session.invalidateAndCancel()
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
        print("PASS: failed downloads stay hidden; completed files read without networking; duplicates reuse saved data")
    }
}

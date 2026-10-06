import Foundation

final class MockAPI: URLProtocol {
    static var requests = 0
    static var status = 200
    static var body = Data()
    static var lastRequest: URLRequest?
    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
        Self.requests += 1
        Self.lastRequest = request
        precondition(request.url?.path == "/api/v1/catalog")
        precondition(request.value(forHTTPHeaderField: "Authorization") == nil)
        client?.urlProtocol(self, didReceive: HTTPURLResponse(url: request.url!, statusCode: Self.status, httpVersion: nil, headerFields: nil)!, cacheStoragePolicy: .notAllowed)
        client?.urlProtocol(self, didLoad: Self.body)
        client?.urlProtocolDidFinishLoading(self)
    }
    override func stopLoading() {}
}
@main struct RemoteCatalogTests {
    static func main() async throws {
        let config = URLSessionConfiguration.ephemeral
        config.protocolClasses = [MockAPI.self]
        let session = URLSession(configuration: config)
        let json = """
        [{"id":"online-pochi","title":"ポチ","genre":"Webtoon","image":"/images/pochi/01.png","tagline":"ポチ","synopsis":"配信中","episodes":[{"id":"pochi","number":1,"title":"ポチ","edition":"配信版","reader":"/?episode=pochi","background":"#111111"}]}]
        """
        MockAPI.body = Data(json.utf8)
        let titles = try await Catalog.loadRemote(session: session)
        precondition(titles.count == 1 && titles[0].episodes[0].number == 1)
        precondition(Catalog.readerURL(titles[0].episodes[0].reader)?.scheme == "https")
        for path in ["//evil.example/x", "https://evil.example/x", "file:///etc/passwd"] {
            precondition(Catalog.remoteURL(path) == nil)
        }
        let cache = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString).appendingPathComponent("catalog.json")
        defer { try? FileManager.default.removeItem(at: cache.deletingLastPathComponent()) }
        var fixture = try JSONSerialization.jsonObject(with: Data(json.utf8)) as! [[String: Any]]
        let first = (fixture[0]["episodes"] as! [[String: Any]])[0]
        var second = first; second["id"] = "second"; second["number"] = 2
        fixture[0]["episodes"] = [second, first]
        MockAPI.body = try JSONSerialization.data(withJSONObject: fixture)
        let sorted = try await Catalog.loadRemote(session: session, cacheURL: cache)
        precondition(sorted[0].orderedEpisodes.map(\.number) == [1, 2])
        precondition(sorted[0].primaryEpisodes.first!.number == 1)
        let count = MockAPI.requests
        let cached = Catalog.cachedRemote(cacheURL: cache)
        precondition(cached?.first?.primaryEpisodes.first?.number == 1 && count == MockAPI.requests)
        print("PASS: chapter 1 stays first and saved catalog appears without a network request")
        fixture[0]["title"] = "ポチ・更新版"
        var third = first; third["id"] = "third"; third["number"] = 3
        fixture[0]["episodes"] = [third, second, first]
        MockAPI.body = try JSONSerialization.data(withJSONObject: fixture)
        let refreshed = try await Catalog.loadRemote(session: session, cacheURL: cache, forceRefresh: true)
        precondition(MockAPI.requests == count + 1)
        precondition(refreshed[0].title == "ポチ・更新版" && refreshed[0].episodeCount == 3)
        precondition(Catalog.cachedRemote(cacheURL: cache)?.first?.episodeCount == 3)
        precondition(MockAPI.lastRequest?.cachePolicy == .reloadIgnoringLocalCacheData)
        precondition(MockAPI.lastRequest?.value(forHTTPHeaderField: "Cache-Control") == "no-cache")
        precondition(URLComponents(url: MockAPI.lastRequest!.url!, resolvingAgainstBaseURL: false)?.queryItems?.first?.name == "refresh")
        print("PASS: manual refresh fetches new chapters, bypasses cached requests, and replaces the saved catalog")
        MockAPI.status = 503
        do { _ = try await Catalog.loadRemote(session: session, cacheURL: cache, forceRefresh: true); fatalError("503 accepted") } catch {}
        precondition(Catalog.cachedRemote(cacheURL: cache)?.first?.episodeCount == 3)
        MockAPI.status = 200
        MockAPI.body = Data(json.replacingOccurrences(of: "/images/pochi/01.png", with: "//evil.example/cover.png").utf8)
        do { _ = try await Catalog.loadRemote(session: session); fatalError("External URL accepted") } catch {}
        print("PASS: remote catalog decoding, HTTP errors, origin restriction, and no admin credentials")
    }
}

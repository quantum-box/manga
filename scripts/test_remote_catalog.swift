import Foundation

final class MockAPI: URLProtocol {
    static var status = 200
    static var body = Data()
    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
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
        MockAPI.status = 503
        do { _ = try await Catalog.loadRemote(session: session); fatalError("503 accepted") } catch {}
        MockAPI.status = 200
        MockAPI.body = Data(json.replacingOccurrences(of: "/images/pochi/01.png", with: "//evil.example/cover.png").utf8)
        do { _ = try await Catalog.loadRemote(session: session); fatalError("External URL accepted") } catch {}
        print("PASS: remote catalog decoding, HTTP errors, origin restriction, and no admin credentials")
    }
}

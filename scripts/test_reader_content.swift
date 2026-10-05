import Foundation
final class ContentAPI: URLProtocol {
    static var status = 200
    static var body = Data()
    static var calls = [String]()
    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }
    override func startLoading() {
        Self.calls.append(request.url!.path)
        precondition(request.value(forHTTPHeaderField: "Authorization") == nil)
        client?.urlProtocol(self, didReceive: HTTPURLResponse(url: request.url!, statusCode: Self.status, httpVersion: nil, headerFields: ["ETag":"W/\"actual-content-revision\""])!, cacheStoragePolicy: .notAllowed)
        client?.urlProtocol(self, didLoad: Self.body)
        client?.urlProtocolDidFinishLoading(self)
    }
    override func stopLoading() {}
}
@main struct ReaderContentTests {
    static func main() async throws {
        ContentAPI.body = Data("""
        {"title":"Website metadata","subtitle":"Not part of the comic","blocks":[{"type":"image","src":"retina-1.png","alt":"<title>"},{"type":"caption","text":"<script>bad()</script>"},{"type":"image","src":"retina-2.png","alt":"next"}]}
        """.utf8)
        let configuration = URLSessionConfiguration.ephemeral; configuration.protocolClasses = [ContentAPI.self]
        let session = URLSession(configuration: configuration)
        let result = try await ReaderContent.load(id: "chapter-1", session: session)
        precondition(ContentAPI.calls == ["/api/episodes/chapter-1"])
        precondition(result.revision == "actual-content-revision")
        precondition(!result.html.contains("Website metadata") && !result.html.contains("<nav") && !result.html.contains("<header"))
        precondition(!result.html.contains("<script>") && result.html.contains("&lt;script&gt;"))
        precondition(result.html.contains("/images/chapter-1/retina-1.png") && result.html.contains("loading=\"eager\"") && result.html.contains("loading=\"lazy\""))
        ContentAPI.status = 503
        do { _ = try await ReaderContent.load(id: "chapter-1", session: session); fatalError("Error document accepted") } catch {}
        ContentAPI.status = 200
        ContentAPI.body = Data("{\"blocks\":[{\"type\":\"image\",\"src\":\"../secret.png\"}]}".utf8)
        do { _ = try await ReaderContent.load(id: "chapter-1", session: session); fatalError("Traversal accepted") } catch {}
        let count = ContentAPI.calls.count
        do { _ = try await ReaderContent.load(id: "../bad", session: session); fatalError("Invalid chapter accepted") } catch {}
        precondition(ContentAPI.calls.count == count)
        print("PASS: reader requests only the chapter JSON, keeps its actual revision, renders only content, and rejects errors and unsafe paths")
    }
}

import SwiftUI
import WebKit

// Exercise the production ReaderView inside its navigation and tab containers.
private struct ScrollTestRoot: View {
    let title: MangaTitle
    @State private var path = [Episode]()

    var body: some View {
        TabView {
            NavigationStack(path: $path) {
                Text("Reader scroll test")
                    .navigationTitle("Catalog")
                    .navigationDestination(for: Episode.self) { ReaderView(title: title, episode: $0) }
                    .task {
                        guard path.isEmpty else { return }
                        try? await Task.sleep(for: .milliseconds(300))
                        // Use the last chapter so reaching the bottom cannot open an alert.
                        path.append(title.episodes[2])
                    }
            }.tabItem { Label("Home", systemImage: "house") }
            Text("Settings").tabItem { Label("Settings", systemImage: "gearshape") }
        }
    }
}

@main
final class ScrollTestApp: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, configurationForConnecting session: UISceneSession,
                     options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        let configuration = UISceneConfiguration(name: "Reader scroll test", sessionRole: session.role)
        configuration.delegateClass = ScrollTestScene.self
        return configuration
    }
}

final class ScrollTestScene: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    private var maximumDelta = 0.0
    private var measurements = 0

    private struct Failure: Error, CustomStringConvertible {
        let description: String
    }

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options: UIScene.ConnectionOptions) {
        guard let scene = scene as? UIWindowScene else { return }
        let episodes = (1...3).map {
            Episode(id: "scroll-test-\($0)", number: $0, title: "Chapter \($0)", edition: "",
                    reader: "scroll-test/index.html", background: "#ffffff")
        }
        let title = MangaTitle(id: "scroll-test", title: "Scroll test", genre: "Test", image: "",
                               tagline: "", synopsis: "", episodes: episodes)
        let window = UIWindow(windowScene: scene)
        window.rootViewController = UIHostingController(rootView: ScrollTestRoot(title: title))
        self.window = window
        window.makeKeyAndVisible()
        Task { @MainActor in
            do {
                let view = try await self.loadedReader(in: window)
                try await self.check(view, in: window)
                self.finish(error: nil)
            } catch {
                self.finish(error: String(describing: error))
            }
        }
    }

    private func findReader(in root: UIView) -> WKWebView? {
        if let view = root as? WKWebView { return view }
        return root.subviews.lazy.compactMap { self.findReader(in: $0) }.first
    }

    private func loadedReader(in window: UIWindow) async throws -> WKWebView {
        for _ in 0..<150 {
            try await Task.sleep(for: .milliseconds(100))
            guard let view = findReader(in: window), !view.isLoading, view.scrollView.contentSize.height > 3000,
                  let coordinator = view.navigationDelegate as? WebtoonReader.Coordinator,
                  case .ready = coordinator.loadState.wrappedValue else { continue }
            try await Task.sleep(for: .milliseconds(500))
            return view
        }
        throw Failure(description: "The production reader did not load the local chapter")
    }

    private func measure(_ view: WKWebView, in window: UIWindow) async throws -> [String: Double] {
        let frame = view.convert(view.bounds, to: window)
        let scroll = view.scrollView
        let inset = scroll.adjustedContentInset
        var values = ["frameX": Double(frame.minX), "frameY": Double(frame.minY),
                      "frameWidth": Double(frame.width), "frameHeight": Double(frame.height),
                      "offsetX": Double(scroll.contentOffset.x), "offsetY": Double(scroll.contentOffset.y),
                      "insetTop": Double(inset.top), "insetBottom": Double(inset.bottom)]
        guard let dom = try await view.evaluateJavaScript("""
            ({scrollY, viewportHeight: innerHeight, viewportWidth: innerWidth,
              scale: visualViewport.scale, markerTop: document.getElementById('marker').getBoundingClientRect().top})
            """) as? [String: NSNumber] else {
            throw Failure(description: "Cannot measure the rendered chapter")
        }
        for (key, value) in dom { values[key] = value.doubleValue }
        return values
    }

    private func assertStable(_ view: WKWebView, in window: UIWindow, baseline: [String: Double],
                              context: String) async throws {
        // Sample during the 0.2-second fade as well as after it finishes.
        for _ in 0..<6 {
            try await Task.sleep(for: .milliseconds(50))
            let current = try await measure(view, in: window)
            measurements += 1
            for (key, expected) in baseline {
                guard let actual = current[key] else { throw Failure(description: "Missing measurement: \(key)") }
                let delta = abs(actual - expected)
                maximumDelta = max(maximumDelta, delta)
                if delta > 0.5 {
                    throw Failure(description: "\(context): \(key) moved from \(expected) to \(actual) (\(delta)pt)")
                }
            }
            guard findReader(in: window) === view else {
                throw Failure(description: "\(context): toggling controls replaced the web view")
            }
        }
    }

    private func screenshot(_ window: UIWindow) throws -> Data {
        let renderer = UIGraphicsImageRenderer(bounds: window.bounds)
        let image = renderer.image { _ in window.drawHierarchy(in: window.bounds, afterScreenUpdates: true) }
        guard let data = image.pngData() else { throw Failure(description: "Cannot capture reader controls") }
        return data
    }

    private func check(_ view: WKWebView, in window: UIWindow) async throws {
        guard let coordinator = view.navigationDelegate as? WebtoonReader.Coordinator else {
            throw Failure(description: "The production reader coordinator is missing")
        }
        let end = view.scrollView.contentSize.height - view.bounds.height
        for (position, y) in [("top", CGFloat.zero), ("middle", end / 2), ("bottom", end)] {
            view.scrollView.setContentOffset(CGPoint(x: 0, y: y), animated: false)
            try await Task.sleep(for: .milliseconds(300))
            let baseline = try await measure(view, in: window)
            for cycle in 1...3 {
                let shown = try screenshot(window)
                coordinator.scrollViewWillBeginDragging(view.scrollView)
                try await assertStable(view, in: window, baseline: baseline, context: "\(position), hide \(cycle)")
                let hidden = try screenshot(window)
                guard shown != hidden else { throw Failure(description: "\(position): scrolling did not hide controls") }
                coordinator.readerTapped()
                try await assertStable(view, in: window, baseline: baseline, context: "\(position), show \(cycle)")
                guard try screenshot(window) != hidden else {
                    throw Failure(description: "\(position): tapping did not show controls")
                }
            }
        }
    }

    private func finish(error: String?) {
        let result: [String: Any] = ["passed": error == nil, "error": error ?? "",
                                     "maximumDelta": maximumDelta, "measurements": measurements,
                                     "systemVersion": UIDevice.current.systemVersion]
        do {
            let file = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
                .appendingPathComponent("reader-scroll-result.json")
            try JSONSerialization.data(withJSONObject: result, options: [.sortedKeys]).write(to: file, options: .atomic)
        } catch {
            print("Cannot write reader scroll result: \(error)")
        }
        exit(error == nil ? 0 : 1)
    }
}

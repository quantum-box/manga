import SwiftUI
import WebKit

@main
struct MangaApp: App {
    var body: some Scene {
        WindowGroup { MainTabView().tint(.orange) }
    }
}

struct MainTabView: View {
    var body: some View {
        TabView {
            NavigationStack { CatalogView() }
                .tabItem { Label("ホーム", systemImage: "house") }
            NavigationStack { DownloadSettingsView() }
                .tabItem { Label("設定", systemImage: "gearshape") }
        }
    }
}

struct Cover: View {
    let name: String
    var body: some View {
        if let url = Catalog.remoteURL(name) {
            AsyncImage(url: url) { image in image.resizable().scaledToFill() }
                placeholder: { Rectangle().fill(.orange.opacity(0.15)).overlay { ProgressView() } }
        } else if let url = Catalog.resource(name),
           let image = UIImage(contentsOfFile: url.path) {
            Image(uiImage: image).resizable().scaledToFill()
        } else {
            Rectangle().fill(.orange.opacity(0.15)).overlay { Image(systemName: "book.closed") }
        }
    }
}

struct CatalogView: View {
    let online: Bool
    @State private var catalog: Result<[MangaTitle], Error>
    @State private var loading = true
    @State private var refreshError: String?
    @State private var lastUpdated: Date?
    @State private var selectedTitle: MangaTitle?

    init(online: Bool = true) {
        self.online = online
        let offline = (try? Catalog.loadOffline()) ?? []
        _catalog = State(initialValue: .success(online ? (Catalog.cachedRemote() ?? offline) : offline))
    }

    @MainActor private func refresh(forceRefresh: Bool = false) async {
        loading = true
        defer { loading = false }
        refreshError = nil
        if online {
            do {
                let titles = try await Catalog.loadRemote(cacheURL: Catalog.remoteCacheURL, forceRefresh: forceRefresh)
                guard !Task.isCancelled else { return }
                catalog = .success(titles)
                lastUpdated = Date()
            }
            catch {
                guard !Task.isCancelled else { return }
                if catalogTitles.isEmpty { catalog = .failure(error) }
                else { refreshError = "一覧を更新できませんでした。通信を確認して再読み込みしてください。" }
            }
        } else { catalog = Result { try Catalog.loadOffline() } }
        if !genres.contains(genre) { genre = "すべて" }
    }
    @State private var query = ""
    @State private var genre = "すべて"
    private var catalogTitles: [MangaTitle] { (try? catalog.get()) ?? [] }
    private var catalogFailed: Bool {
        if case .failure = catalog { return true }
        return false
    }
    private var genres: [String] { ["すべて"] + Array(Set(catalogTitles.map(\.genre))).sorted() }
    private var titles: [MangaTitle] {
        catalogTitles.filter { (genre == "すべて" || $0.genre == genre) && (query.isEmpty || $0.title.localizedCaseInsensitiveContains(query)) }
    }

    var body: some View {
        List {
            VStack(alignment: .leading, spacing: 24) {
                if online {
                    HStack {
                        VStack(alignment: .leading, spacing: 4) {
                            Text("MANGA").font(.system(size: 30, weight: .black, design: .rounded))
                            Text("今日も、物語に出会おう。").font(.subheadline).foregroundStyle(.secondary)
                        }
                        Spacer()
                    }
                    if let lastUpdated {
                        Text("一覧を更新 \(lastUpdated.formatted(date: .omitted, time: .standard))")
                            .font(.caption).foregroundStyle(.secondary)
                            .accessibilityIdentifier("catalog-updated")
                    }
                } else {
                    Text("保存済みの作品と同梱作品を、通信なしで読めます。")
                        .font(.subheadline).foregroundStyle(.secondary)
                }
                if loading { ProgressView("一覧を更新中…") }
                if let refreshError {
                    VStack(alignment: .leading, spacing: 8) {
                        Text(refreshError).font(.subheadline).foregroundStyle(.secondary)
                        Button("再読み込み") { Task { await refresh(forceRefresh: true) } }
                    }.accessibilityIdentifier("catalog-refresh-failed")
                }
                if query.isEmpty && genre == "すべて", let featured = catalogTitles.first {
                    Button { selectedTitle = featured } label: {
                        GeometryReader { proxy in
                            ZStack(alignment: .bottomLeading) {
                                Cover(name: featured.image).frame(width: proxy.size.width, height: proxy.size.height).clipped()
                                LinearGradient(colors: [.clear, .black.opacity(0.85)], startPoint: .center, endPoint: .bottom)
                                VStack(alignment: .leading, spacing: 8) {
                                    Text("PICK UP").font(.caption.bold()).padding(.horizontal, 10).padding(.vertical, 5).background(.orange, in: Capsule())
                                    Text(featured.tagline).font(.title2.bold())
                                    Text(featured.title).font(.subheadline.bold())
                                    Text("第1話を無料で読む  →").font(.caption.bold())
                                }.foregroundStyle(.white).padding(20)
                            }.frame(width: proxy.size.width, height: proxy.size.height)
                        }.frame(height: 290).clipShape(RoundedRectangle(cornerRadius: 20))
                    }.buttonStyle(.plain).accessibilityIdentifier("featured-title")
                }
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 8) {
                        ForEach(genres, id: \.self) { item in
                            Button { genre = item } label: {
                                Text(item).font(.subheadline.bold()).padding(.horizontal, 16).padding(.vertical, 10)
                                    .background(genre == item ? Color.primary : Color(.secondarySystemBackground), in: Capsule())
                                    .foregroundStyle(genre == item ? Color(.systemBackground) : Color.primary)
                            }
                        }
                    }
                }
                HStack {
                    Text(query.isEmpty ? "作品を探す" : "検索結果").font(.title2.bold())
                    Spacer()
                    Text("\(titles.count)作品").font(.caption).foregroundStyle(.secondary)
                }
                if catalogFailed {
                    ContentUnavailableView {
                        Label("作品を読み込めませんでした", systemImage: "exclamationmark.triangle")
                    } description: {
                        Text(online ? "通信を確認して再読み込みしてください。設定のオフラインから保存済み作品を読めます。" : "同梱作品を読み込めません。アプリを更新してください。")
                    } actions: {
                        Button("もう一度読み込む") { Task { await refresh(forceRefresh: true) } }
                            .buttonStyle(.borderedProminent)
                    }.accessibilityIdentifier("catalog-failed")
                } else if !loading && titles.isEmpty {
                    ContentUnavailableView.search(text: query)
                }
                LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 24) {
                    ForEach(titles) { title in
                        Button { selectedTitle = title } label: {
                            VStack(alignment: .leading, spacing: 7) {
                                GeometryReader { proxy in
                                    Cover(name: title.image).frame(width: proxy.size.width, height: proxy.size.height).clipped()
                                }.aspectRatio(0.72, contentMode: .fit).clipShape(RoundedRectangle(cornerRadius: 12))
                                Text(title.genre).font(.caption2.bold()).foregroundStyle(.orange)
                                Text(title.title).font(.subheadline.bold()).lineLimit(2).frame(height: 40, alignment: .topLeading)
                                Text("全\(title.episodeCount)話 · 無料").font(.caption).foregroundStyle(.secondary)
                            }
                        }.buttonStyle(.plain).accessibilityIdentifier("title-\(title.id)")
                    }
                }
                Text("全作品、無料で読めます。").font(.caption2).foregroundStyle(.secondary)
            }.padding(20)
            .listRowInsets(EdgeInsets())
            .listRowSeparator(.hidden)
        }
        .listStyle(.plain)
        .scrollContentBackground(.hidden)
        .accessibilityIdentifier(online ? "home-catalog" : "offline-catalog")
        .background(Color(.systemBackground))
        .navigationTitle(online ? "ホーム" : "オフライン")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar(online ? .hidden : .visible, for: .navigationBar)
        .task { await refresh() }
        .refreshable { await refresh(forceRefresh: true) }
        .searchable(text: $query, prompt: "作品タイトルで検索")
        .navigationDestination(item: $selectedTitle) { TitleDetailView(title: $0) }
    }
}

struct TitleDetailView: View {
    let title: MangaTitle
    @State private var descending = false
    @State private var saved = false
    @AppStorage("autoSaveWebtoons") private var autoSave = true

    @AppStorage(ReadingHistory.storageKey) private var readChapters = "[]"
    @AppStorage("favoriteTitles") private var favoriteIDs = ""
    private var isFavorite: Bool { favoriteIDs.split(separator: ",").contains(Substring(title.id)) }
    private var episodes: [Episode] { descending ? title.primaryEpisodes.reversed() : title.primaryEpisodes }

    private func isRead(_ episode: Episode) -> Bool {
        ReadingHistory.contains(readChapters, titleID: title.id, number: episode.number)
    }
    private var continueEpisode: Episode? { title.primaryEpisodes.first { !isRead($0) } ?? title.primaryEpisodes.first }
    private var hasReadEpisodes: Bool { title.primaryEpisodes.contains { isRead($0) } }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                HStack(alignment: .top, spacing: 18) {
                    Cover(name: title.image).frame(width: 120, height: 170).clipped().clipShape(RoundedRectangle(cornerRadius: 12))
                    VStack(alignment: .leading, spacing: 12) {
                        Text(title.genre).font(.caption.bold()).foregroundStyle(.orange)
                        Text(title.title).font(.title2.bold())
                        Text("Quantum Stories").font(.caption).foregroundStyle(.secondary)
                        Text("全\(title.episodeCount)話 · 全話無料").font(.caption.bold())
                    }
                }
                Text(title.synopsis).font(.subheadline).foregroundStyle(.secondary).lineSpacing(5)
                HStack(spacing: 12) {
                    if let first = continueEpisode {
                        NavigationLink { ReaderView(title: title, episode: first) } label: {
                            Label(hasReadEpisodes && !isRead(first) ? "続きから読む · 第\(first.number)話" : "第\(first.number)話から読む", systemImage: "book.fill").font(.subheadline.bold()).frame(maxWidth: .infinity).padding(.vertical, 15)
                        }.buttonStyle(.borderedProminent)
                    }
                    Button {
                        var ids = favoriteIDs.split(separator: ",").map(String.init)
                        if isFavorite { ids.removeAll { $0 == title.id } } else { ids.append(title.id) }
                        favoriteIDs = ids.joined(separator: ",")
                    } label: { Image(systemName: isFavorite ? "bookmark.fill" : "bookmark").padding(12) }
                        .buttonStyle(.bordered).accessibilityLabel(isFavorite ? "お気に入りから削除" : "お気に入りに追加")
                }
                if Catalog.remoteURL(title.image) != nil {
                    Label(saved ? "オフライン保存済み" : (autoSave ? "表示後に読んだ話だけ保存" : "自動保存はオフ"), systemImage: saved ? "checkmark.circle.fill" : "arrow.down.circle")
                        .font(.caption).foregroundStyle(.secondary)
                }
                Divider()
                HStack {
                    Text("話一覧").font(.title3.bold())
                    Text("\(title.episodeCount)話").font(.caption).foregroundStyle(.secondary)
                    Spacer()
                    Button { descending.toggle() } label: {
                        Label(descending ? "新しい順" : "古い順", systemImage: "arrow.up.arrow.down").font(.caption)
                    }
                }
                VStack(spacing: 0) {
                    ForEach(episodes) { episode in
                        NavigationLink { ReaderView(title: title, episode: episode) } label: {
                            HStack(spacing: 14) {
                                Cover(name: title.image).frame(width: 70, height: 58).clipped().clipShape(RoundedRectangle(cornerRadius: 8))
                                VStack(alignment: .leading, spacing: 5) {
                                    Text("第\(episode.number)話").font(.caption).foregroundStyle(.secondary)
                                    Text(episode.title).font(.subheadline.bold())
                                    if !episode.edition.isEmpty {
                                        Text(episode.edition).font(.caption).foregroundStyle(.secondary)
                                    }
                                }
                                Spacer()
                                if isRead(episode) {
                                    Label("既読", systemImage: "checkmark.circle.fill").font(.caption).foregroundStyle(.secondary)
                                } else {
                                    Text("未読").font(.caption).foregroundStyle(.orange)
                                }
                                Image(systemName: "chevron.right").font(.caption).foregroundStyle(.tertiary)
                            }.padding(.vertical, 14)
                        }.buttonStyle(.plain).accessibilityIdentifier("episode-\(episode.id)")
                        .contextMenu {
                            Button(isRead(episode) ? "未読に戻す" : "既読にする") {
                                readChapters = ReadingHistory.setting(!isRead(episode), in: readChapters, titleID: title.id, number: episode.number)
                            }
                        }
                        let editions = title.otherEditions(of: episode)
                        if !editions.isEmpty {
                            DisclosureGroup("ほかの版（\(editions.count)）") {
                                ForEach(editions) { edition in
                                    NavigationLink { ReaderView(title: title, episode: edition) } label: {
                                        Text(edition.edition.isEmpty ? edition.title : edition.edition)
                                            .font(.caption).padding(.vertical, 10)
                                    }
                                }
                            }.font(.caption).padding(.vertical, 8)
                        }
                        Divider()
                    }
                }
            }.padding(20)
        }.navigationTitle("作品詳細").navigationBarTitleDisplayMode(.inline)
        .onAppear { saved = OfflineDownloads.isSaved(title) }
    }
}

struct ReaderView: View {
    let title: MangaTitle
    @Environment(\.dismiss) private var dismiss
    @State private var episode: Episode
    @State private var loadState = ReaderLoadState.loading
    @State private var reloadID = UUID()
    @AppStorage("autoSaveWebtoons") private var autoSave = true
    @State private var saveStatus = ""
    @State private var contentRevision: String?
    @State private var saveDetailsPresented = false
    @State private var controlsVisible = true
    @State private var nextEpisodePresented = false
    @State private var offeredNextEpisode = false
    @AppStorage(ReadingHistory.storageKey) private var readChapters = "[]"


    init(title: MangaTitle, episode: Episode) {
        self.title = title
        _episode = State(initialValue: episode)
    }

    private var previous: Episode? { title.primaryEpisodes.first { $0.number == episode.number - 1 } }
    private var next: Episode? { title.primaryEpisodes.first { $0.number == episode.number + 1 } }

    private func openEpisode(_ destination: Episode) {
        contentRevision = nil
        loadState = .loading
        controlsVisible = true
        nextEpisodePresented = false
        offeredNextEpisode = false
        episode = destination
    }

    private func setControlsVisible(_ visible: Bool) {
        withAnimation(.easeInOut(duration: 0.2)) { controlsVisible = visible }
    }

    var body: some View {
        Group {
            if let url = Catalog.readerURL(episode.reader) {
                ZStack {
                    WebtoonReader(url: url, background: episode.background, loadState: $loadState, onRevision: { contentRevision = $0 }, onNavigate: { destination in
                        if title.linksToChapterList(to: destination) { dismiss() }
                        else if let linked = title.linkedEpisode(to: destination) { openEpisode(linked) }
                    }, onScroll: {
                        if loadState == .ready { setControlsVisible(false) }
                    }, onTap: {
                        setControlsVisible(!controlsVisible)
                    }, onReachEnd: {
                        guard loadState == .ready, next != nil, !offeredNextEpisode else { return }
                        offeredNextEpisode = true
                        nextEpisodePresented = true
                    })
                        .id("\(episode.id)-\(reloadID)")
                        .accessibilityIdentifier("webtoon-reader")
                    if loadState == .loading {
                        ProgressView("漫画を読み込み中…")
                            .padding(24)
                            .background(.regularMaterial, in: RoundedRectangle(cornerRadius: 16))
                            .accessibilityIdentifier("reader-loading")
                    } else if loadState == .failed {
                        ContentUnavailableView {
                            Label("漫画を開けませんでした", systemImage: "book.closed")
                        } description: {
                            Text("もう一度読み込んでください。")
                        } actions: {
                            Button("もう一度読む") {
                                loadState = .loading
                                controlsVisible = true
                                offeredNextEpisode = false
                                nextEpisodePresented = false
                                reloadID = UUID()
                            }.buttonStyle(.borderedProminent)
                        }
                        .background(Color(.systemBackground))
                        .accessibilityIdentifier("reader-failed")
                    }
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                ContentUnavailableView("本文を開けません", systemImage: "book.closed", description: Text("作品一覧に戻って、もう一度お試しください。"))
            }
        }
        .task(id: "\(episode.id)-\(loadState)", priority: .background) {
            guard loadState == .ready else { saveStatus = ""; return }
            readChapters = ReadingHistory.setting(true, in: readChapters, titleID: title.id, number: episode.number)
            guard autoSave, Catalog.remoteURL(title.image) != nil else { return }
            // Give the visible reader priority over optional offline work.
            do { try await Task.sleep(for: .seconds(2)) } catch { return }
            saveStatus = "オフライン保存中…"
            do {
                let downloadedEpisode = Episode(id: episode.id, number: episode.number, title: episode.title, edition: episode.edition,
                    reader: episode.reader, background: episode.background, revision: contentRevision ?? episode.revision)
                let snapshot = MangaTitle(id: title.id, title: title.title, genre: title.genre, image: title.image,
                    tagline: title.tagline, synopsis: title.synopsis,
                    episodes: title.episodes.map { $0.id == episode.id ? downloadedEpisode : $0 }, revision: title.revision)
                try await DownloadManager.shared.download(snapshot, episodeIDs: [episode.id])
                saveStatus = "この話をオフライン保存済み"
            } catch is CancellationError { saveStatus = "" }
              catch { saveStatus = "オフライン保存できませんでした。次に開いたときに再試行します。" }
        }
        .toolbar {
            if !saveStatus.isEmpty {
                ToolbarItem(placement: .topBarTrailing) {
                    Button { saveDetailsPresented = true } label: {
                        Image(systemName: saveStatus.contains("できません") ? "exclamationmark.circle" : (saveStatus.contains("保存済み") ? "checkmark.circle" : "arrow.down.circle"))
                    }.accessibilityLabel(saveStatus)
                }
            }
        }
        .alert("オフライン保存", isPresented: $saveDetailsPresented) { Button("OK", role: .cancel) {} } message: { Text(saveStatus) }
        .alert("次の話を読みますか？", isPresented: $nextEpisodePresented) {
            Button("次の話を読む") { if let next { openEpisode(next) } }
                .accessibilityIdentifier("read-next-episode")
            Button("今は読まない", role: .cancel) {}
        } message: {
            if let next { Text("第\(next.number)話「\(next.title)」") }
        }
        .navigationTitle("第\(episode.number)話\(episode.edition.isEmpty ? "" : " · " + episode.edition)")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar(controlsVisible ? .visible : .hidden, for: .navigationBar)
        .toolbar(.hidden, for: .tabBar)
        .statusBarHidden(!controlsVisible)
        .ignoresSafeArea(.container, edges: controlsVisible ? [] : [.top, .bottom])
        .safeAreaInset(edge: .bottom) {
            if controlsVisible, title.episodeCount > 1 {
                HStack {
                    Button { if let previous { openEpisode(previous) } } label: {
                        Label("前の話", systemImage: "chevron.left")
                    }.disabled(previous == nil).accessibilityIdentifier("previous-episode")
                    Spacer()
                    Text("\(episode.number) / \(title.episodeCount)")
                        .font(.caption).foregroundStyle(.secondary)
                    Spacer()
                    Button { if let next { openEpisode(next) } } label: {
                        HStack(spacing: 5) {
                            Text("次の話")
                            Image(systemName: "chevron.right")
                        }
                    }.disabled(next == nil).accessibilityIdentifier("next-episode")
                }
                .font(.subheadline.bold()).padding(.horizontal, 20).padding(.vertical, 12)
                .background(Color(.systemBackground))
            }
        }
    }
}

enum ReaderLoadState {
    case loading, ready, failed
}

struct WebtoonReader: UIViewRepresentable {
    let url: URL
    let background: String
    @Binding var loadState: ReaderLoadState
    let onRevision: (String) -> Void
    let onNavigate: (URL) -> Void
    let onScroll: () -> Void
    let onTap: () -> Void
    let onReachEnd: () -> Void

    func makeCoordinator() -> Coordinator {
        Coordinator(loadState: $loadState, onRevision: onRevision, onNavigate: onNavigate,
                    onScroll: onScroll, onTap: onTap, onReachEnd: onReachEnd)
    }

    func makeUIView(context: Context) -> WKWebView {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .nonPersistent()
        configuration.userContentController.add(context.coordinator, name: "mangaReader")
        // Image loads can extend a lazy-loaded chapter after scrolling appears to reach its end.
        configuration.userContentController.addUserScript(WKUserScript(source: """
            (() => {
              let scheduled = false;
              const schedule = () => {
                if (scheduled) return;
                scheduled = true;
                requestAnimationFrame(() => {
                  scheduled = false;
                  const page = document.scrollingElement;
                  if (!page || page.scrollTop + page.clientHeight < page.scrollHeight - 24) return;
                  if (Array.from(document.images).some(image => !image.complete || image.naturalWidth === 0)) return;
                  window.webkit.messageHandlers.mangaReader.postMessage({state: 'reachedEnd'});
                });
              };
              document.addEventListener('scroll', schedule, {passive: true});
              document.addEventListener('load', schedule, true);
              document.addEventListener('touchend', schedule, {passive: true});
              window.addEventListener('resize', schedule);
              new ResizeObserver(schedule).observe(document.documentElement);
            })();
            """, injectionTime: .atDocumentEnd, forMainFrameOnly: true))
        if !url.isFileURL, let id = ReaderContent.episodeID(from: url) {
            // This script runs only in our API-derived document, never in the website shell.
            let quotedID = String(data: try! JSONEncoder().encode(id), encoding: .utf8)!
            configuration.userContentController.addUserScript(WKUserScript(source: """
                (() => {
                  const notify = state => window.webkit.messageHandlers.mangaReader.postMessage({state, episodeID: \(quotedID)});
                  const image = document.images[0];
                  if (!image) notify('ready');
                  else if (image.complete) notify(image.naturalWidth > 0 ? 'ready' : 'failed');
                  else { image.addEventListener('load', () => notify('ready'), {once:true}); image.addEventListener('error', () => notify('failed'), {once:true}); }
                })();
                """, injectionTime: .atDocumentEnd, forMainFrameOnly: true))
        }
        let view = WKWebView(frame: .zero, configuration: configuration)
        view.navigationDelegate = context.coordinator
        view.scrollView.delegate = context.coordinator
        let tap = UITapGestureRecognizer(target: context.coordinator, action: #selector(Coordinator.readerTapped))
        tap.cancelsTouchesInView = false
        tap.delegate = context.coordinator
        view.addGestureRecognizer(tap)
        let color = UIColor(webtoonHex: background)
        view.isOpaque = false
        view.backgroundColor = color
        view.scrollView.backgroundColor = color
        view.scrollView.contentInsetAdjustmentBehavior = .never
        view.scrollView.alwaysBounceHorizontal = false
        context.coordinator.load(url, in: view)
        return view
    }

    func updateUIView(_ view: WKWebView, context: Context) {
        context.coordinator.loadState = $loadState
        context.coordinator.onRevision = onRevision
        context.coordinator.onNavigate = onNavigate
        context.coordinator.onScroll = onScroll
        context.coordinator.onTap = onTap
        context.coordinator.onReachEnd = onReachEnd
        context.coordinator.load(url, in: view)
    }

    static func dismantleUIView(_ view: WKWebView, coordinator: Coordinator) {
        coordinator.contentTask?.cancel()
        view.configuration.userContentController.removeScriptMessageHandler(forName: "mangaReader")
        view.navigationDelegate = nil
        view.scrollView.delegate = nil
        view.stopLoading()
    }

    final class Coordinator: NSObject, WKNavigationDelegate, WKScriptMessageHandler, UIScrollViewDelegate, UIGestureRecognizerDelegate {
        var loadState: Binding<ReaderLoadState>
        private var requestedURL: URL?
        var contentTask: Task<Void, Never>?
        var onRevision: (String) -> Void
        var onNavigate: (URL) -> Void
        var onScroll: () -> Void
        var onTap: () -> Void
        var onReachEnd: () -> Void
        private var hasUserScrolled = false

        init(loadState: Binding<ReaderLoadState>, onRevision: @escaping (String) -> Void, onNavigate: @escaping (URL) -> Void,
             onScroll: @escaping () -> Void, onTap: @escaping () -> Void, onReachEnd: @escaping () -> Void) {
            self.loadState = loadState; self.onRevision = onRevision; self.onNavigate = onNavigate
            self.onScroll = onScroll; self.onTap = onTap; self.onReachEnd = onReachEnd
        }

        func scrollViewWillBeginDragging(_ scrollView: UIScrollView) {
            hasUserScrolled = true
            onScroll()
        }

        @objc func readerTapped() { onTap() }

        func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer,
                               shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool { true }

        func load(_ url: URL, in view: WKWebView) {
            guard requestedURL != url else { return }
            requestedURL = url
            hasUserScrolled = false
            contentTask?.cancel()
            if url.isFileURL {
                view.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
            } else {
                contentTask = Task { @MainActor [weak self, weak view] in
                    do {
                        guard let id = ReaderContent.episodeID(from: url) else { throw ReaderContent.ContentError.invalidContent }
                        let content = try await ReaderContent.load(id: id)
                        try Task.checkCancellation()
                        guard let self, let view, self.requestedURL == url else { return }
                        self.onRevision(content.revision)
                        view.loadHTMLString(content.html, baseURL: Catalog.apiBaseURL)
                    } catch {
                        if !Task.isCancelled, self?.requestedURL == url { self?.loadState.wrappedValue = .failed }
                    }
                }
            }
        }

        func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
            loadState.wrappedValue = .loading
        }

        func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
                     decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
            // Episode and chapter-list links are handled natively without loading another directory.
            if navigationAction.navigationType == .linkActivated {
                decisionHandler(.cancel)
                if requestedURL?.isFileURL == true, let destination = navigationAction.request.url {
                    onNavigate(destination)
                }
            } else { decisionHandler(.allow) }
        }

        func webView(_ webView: WKWebView, decidePolicyFor navigationResponse: WKNavigationResponse,
                     decisionHandler: @escaping (WKNavigationResponsePolicy) -> Void) {
            if navigationResponse.isForMainFrame,
               let response = navigationResponse.response as? HTTPURLResponse,
               response.statusCode >= 400 {
                loadState.wrappedValue = .failed
                decisionHandler(.cancel)
            } else { decisionHandler(.allow) }
        }

        func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
            // Remote documents wait for the first image before being marked ready.
            if requestedURL?.isFileURL == true { loadState.wrappedValue = .ready }
        }

        func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
            guard message.frameInfo.isMainFrame,
                  message.name == "mangaReader", let body = message.body as? [String: String] else { return }
            if body["state"] == "reachedEnd" {
                guard hasUserScrolled, loadState.wrappedValue == .ready, let scrollView = message.webView?.scrollView,
                      scrollView.contentSize.height > 0,
                      scrollView.contentOffset.y + scrollView.bounds.height >= scrollView.contentSize.height - 24 else { return }
                onReachEnd()
                return
            }
            guard let requestedURL, !requestedURL.isFileURL,
                  let expectedID = URLComponents(url: requestedURL, resolvingAgainstBaseURL: false)?.queryItems?.first(where: { $0.name == "episode" })?.value,
                  body["episodeID"] == expectedID else { return }
            if body["state"] == "ready" { loadState.wrappedValue = .ready }
            else if body["state"] == "failed" { loadState.wrappedValue = .failed }
        }

        func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
            loadState.wrappedValue = .failed
        }

        func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
            loadState.wrappedValue = .failed
        }

        func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
            loadState.wrappedValue = .failed
        }
    }
}

private extension UIColor {
    convenience init(webtoonHex: String) {
        let value = UInt32(webtoonHex.dropFirst(), radix: 16) ?? 0xffffff
        self.init(red: CGFloat((value >> 16) & 255) / 255,
                  green: CGFloat((value >> 8) & 255) / 255,
                  blue: CGFloat(value & 255) / 255, alpha: 1)
    }
}

#Preview { MainTabView() }


struct DownloadSettingsView: View {
    @AppStorage("autoSaveWebtoons") private var autoSave = true
    @State private var titles = [MangaTitle]()
    @State private var selected: MangaTitle?
    @State private var confirmDelete = false
    @State private var error = ""
    private func reload() {
        do { titles = try OfflineDownloads.load(); error = "" }
        catch { self.error = "保存済み作品を読み込めませんでした。" }
    }
    var body: some View {
        Form {
            Section("ライブラリ") {
                NavigationLink { CatalogView(online: false) } label: {
                    Label("オフライン", systemImage: "arrow.down.circle")
                }.accessibilityIdentifier("offline-library")
            }
            Section {
                Toggle("表示後に読んだ話だけ保存", isOn: $autoSave)
            } footer: {
                Text("作品を開くと、本文と画像を端末内へ保存します。保存中はアプリを開いておいてください。")
            }
            Section("端末に保存した作品") {
                if titles.isEmpty { Text("保存済み作品はありません").foregroundStyle(.secondary) }
                ForEach(titles) { title in
                    HStack {
                        Text(title.title)
                        Spacer()
                        Button("削除", role: .destructive) { selected = title; confirmDelete = true }
                            .accessibilityIdentifier("delete-\(title.id)")
                    }
                }
            }
            Section {
                Text("削除した作品は、次に配信から開くと再保存します。再保存を止めるには自動保存をオフにしてください。同梱作品は削除されません。")
                    .font(.caption).foregroundStyle(.secondary)
                if !error.isEmpty { Text(error).foregroundStyle(.red) }
            }
        }
        .navigationTitle("設定")
        .onAppear { reload() }
        .confirmationDialog("端末の保存データを削除しますか？", isPresented: $confirmDelete, titleVisibility: .visible) {
            Button("端末から削除", role: .destructive) {
                guard let selected else { return }
                Task {
                    do { try await DownloadManager.shared.delete(selected.id); reload() }
                    catch { self.error = "削除できませんでした。もう一度お試しください。" }
                }
            }
        } message: { Text(selected?.title ?? "") }
    }
}

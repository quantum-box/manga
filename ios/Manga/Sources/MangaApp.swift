import SwiftUI
import WebKit

@main
struct MangaApp: App {
    var body: some Scene {
        WindowGroup { CatalogView().tint(.orange) }
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
    @State private var catalog: Result<[MangaTitle], Error> = .success([])
    @State private var online = true
    @State private var settingsPresented = false
    @State private var loading = true
    @MainActor private func refresh() async {
        loading = true
        defer { loading = false }
        genre = "すべて"
        if online {
            do {
                let titles = try await Catalog.loadRemote()
                guard !Task.isCancelled else { return }
                catalog = .success(titles)
            }
            catch { if !Task.isCancelled { catalog = .failure(error) } }
        } else { catalog = Result { try Catalog.loadOffline() } }
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
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 24) {
                    HStack {
                        VStack(alignment: .leading, spacing: 4) {
                            Text("MANGA").font(.system(size: 30, weight: .black, design: .rounded))
                            Text("今日も、物語に出会おう。").font(.subheadline).foregroundStyle(.secondary)
                        }
                        Spacer()
                        Button { settingsPresented = true } label: {
                            Image(systemName: "gearshape").font(.title).foregroundStyle(.orange)
                        }.accessibilityLabel("設定").accessibilityIdentifier("settings")
                    }
                    Picker("読み込み元", selection: $online) {
                        Text("配信").tag(true)
                        Text("オフライン").tag(false)
                    }.pickerStyle(.segmented).accessibilityIdentifier("catalog-source")
                    if loading { ProgressView("作品を取得中…") }
                    if query.isEmpty && genre == "すべて", let featured = catalogTitles.first {
                        NavigationLink(value: featured) {
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
                            Text(online ? "通信を確認して再読み込みしてください。オフラインに切り替えると同梱作品を読めます。" : "同梱作品を読み込めません。アプリを更新してください。")
                        } actions: {
                            Button("もう一度読み込む") { Task { await refresh() } }
                                .buttonStyle(.borderedProminent)
                        }.accessibilityIdentifier("catalog-failed")
                    } else if !loading && titles.isEmpty {
                        ContentUnavailableView.search(text: query)
                    }
                    LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 24) {
                        ForEach(titles) { title in
                            NavigationLink(value: title) {
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
            }
            .background(Color(.systemBackground))
            .toolbar(.hidden, for: .navigationBar)
            .sheet(isPresented: $settingsPresented, onDismiss: { Task { await refresh() } }) { DownloadSettingsView() }
            .task(id: online) { await refresh() }
            .refreshable { await refresh() }
            .searchable(text: $query, prompt: "作品タイトルで検索")
            .navigationDestination(for: MangaTitle.self) { TitleDetailView(title: $0) }
        }
    }
}

struct TitleDetailView: View {
    let title: MangaTitle
    @State private var descending = false
    @State private var saved = false
    @AppStorage("autoSaveWebtoons") private var autoSave = true

    @AppStorage("favoriteTitles") private var favoriteIDs = ""
    private var isFavorite: Bool { favoriteIDs.split(separator: ",").contains(Substring(title.id)) }
    private var episodes: [Episode] { descending ? title.episodes.reversed() : title.episodes }

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
                    if let first = title.episodes.first {
                        NavigationLink { ReaderView(title: title, episode: first) } label: {
                            Label("第1話から読む", systemImage: "book.fill").font(.subheadline.bold()).frame(maxWidth: .infinity).padding(.vertical, 15)
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
                    Label(saved ? "オフライン保存済み" : (autoSave ? "読むと自動でオフラインに保存" : "自動保存はオフ"), systemImage: saved ? "checkmark.circle.fill" : "arrow.down.circle")
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
                                Text("無料").font(.caption.bold()).foregroundStyle(.orange)
                                Image(systemName: "chevron.right").font(.caption).foregroundStyle(.tertiary)
                            }.padding(.vertical, 14)
                        }.buttonStyle(.plain).accessibilityIdentifier("episode-\(episode.id)")
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
    @State private var episode: Episode
    @State private var loadState = ReaderLoadState.loading
    @State private var reloadID = UUID()
    @AppStorage("autoSaveWebtoons") private var autoSave = true
    @State private var saveStatus = ""


    init(title: MangaTitle, episode: Episode) {
        self.title = title
        _episode = State(initialValue: episode)
    }

    private var previous: Episode? { title.episodes.first { $0.number == episode.number - 1 } }
    private var next: Episode? { title.episodes.first { $0.number == episode.number + 1 } }

    var body: some View {
        Group {
            if let url = Catalog.readerURL(episode.reader) {
                ZStack {
                    WebtoonReader(url: url, background: episode.background, loadState: $loadState)
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
        .task(id: title.id) {
            guard autoSave, Catalog.remoteURL(title.image) != nil else { return }
            saveStatus = "オフライン保存中…"
            do {
                try await DownloadManager.shared.download(title)
                saveStatus = "オフライン保存済み"
            } catch is CancellationError { saveStatus = "" }
              catch { saveStatus = "オフライン保存できませんでした。次に開いたときに再試行します。" }
        }
        .overlay(alignment: .bottom) {
            if !saveStatus.isEmpty {
                Text(saveStatus).font(.caption2).padding(8).background(.regularMaterial, in: Capsule()).padding(.bottom, 8)
                    .allowsHitTesting(false).accessibilityIdentifier("auto-save-status")
            }
        }
        .navigationTitle("第\(episode.number)話\(episode.edition.isEmpty ? "" : " · " + episode.edition)")
        .navigationBarTitleDisplayMode(.inline)
        .safeAreaInset(edge: .bottom) {
            if title.episodeCount > 1 {
                HStack {
                    Button { if let previous { loadState = .loading; episode = previous } } label: {
                        Label("前の話", systemImage: "chevron.left")
                    }.disabled(previous == nil).accessibilityIdentifier("previous-episode")
                    Spacer()
                    Text("\(episode.number) / \(title.episodeCount)")
                        .font(.caption).foregroundStyle(.secondary)
                    Spacer()
                    Button { if let next { loadState = .loading; episode = next } } label: {
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

    func makeCoordinator() -> Coordinator { Coordinator(loadState: $loadState) }

    func makeUIView(context: Context) -> WKWebView {
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .nonPersistent()
        let view = WKWebView(frame: .zero, configuration: configuration)
        view.navigationDelegate = context.coordinator
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
        context.coordinator.load(url, in: view)
    }

    static func dismantleUIView(_ view: WKWebView, coordinator: Coordinator) {
        view.navigationDelegate = nil
        view.stopLoading()
    }

    final class Coordinator: NSObject, WKNavigationDelegate {
        var loadState: Binding<ReaderLoadState>
        private var requestedURL: URL?

        init(loadState: Binding<ReaderLoadState>) { self.loadState = loadState }

        func load(_ url: URL, in view: WKWebView) {
            guard requestedURL != url else { return }
            requestedURL = url
            if url.isFileURL {
                view.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
            } else { view.load(URLRequest(url: url)) }
        }

        func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!) {
            loadState.wrappedValue = .loading
        }

        func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
            loadState.wrappedValue = .ready
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

#Preview { CatalogView() }


struct DownloadSettingsView: View {
    @Environment(\.dismiss) private var dismiss
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
        NavigationStack {
            Form {
                Section {
                    Toggle("読んだ作品を自動保存", isOn: $autoSave)
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
            .toolbar { ToolbarItem(placement: .confirmationAction) { Button("完了") { dismiss() } } }
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
}

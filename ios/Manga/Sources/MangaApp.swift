import SwiftUI

@main
struct MangaApp: App {
    var body: some Scene {
        WindowGroup { CatalogView().tint(.orange) }
    }
}

struct MangaTitle: Identifiable, Hashable {
    let id: String
    let title: String
    let genre: String
    let image: String
    let tagline: String
    let synopsis: String
    let episodes: [Episode]
}

struct Episode: Identifiable, Hashable {
    let id: Int
    let title: String
    let panels: [String]
}

enum Catalog {
    static let titles: [MangaTitle] = [
        .init(id: "pochi", title: "柴犬ポチと魔王の「おて」", genre: "ファンタジー", image: "01-rebirth", tagline: "世界を救うのは、小さな肉球。", synopsis: "異世界に転生した柴犬ポチ。お姫さまと出会い、たどり着いたのは魔王の城。最強の魔王に差し出したのは、たったひとつの「おて」だった。", episodes: [.init(id: 1, title: "世界を救う、小さな「おて」", panels: ["01-rebirth", "02-princess", "03-demon-king", "04-handshake"])]),
        .init(id: "moon", title: "月明かりの約束", genre: "恋愛", image: "02-princess", tagline: "あの日の約束を、もう一度。", synopsis: "お城で暮らす少女と、不思議な旅人。月明かりの下で始まる、小さな出会いの物語。※画面確認用のサンプル作品です。", episodes: (1...6).map { .init(id: $0, title: ["月夜の出会い", "秘密の庭", "届かない手紙", "約束の日", "君の名前", "夜明けの前に"][$0 - 1], panels: []) }),
        .init(id: "king", title: "魔王の休日", genre: "ファンタジー", image: "03-demon-king", tagline: "今日だけは、世界征服お休み。", synopsis: "恐れられる魔王にも、のんびり過ごしたい日がある。魔王城の日常を描くコメディ。※画面確認用のサンプル作品です。", episodes: (1...4).map { .init(id: $0, title: ["魔王、休む", "お客さま", "お茶の時間", "明日も休日"][$0 - 1], panels: []) }),
        .init(id: "paw", title: "肉球と世界のあいだ", genre: "日常", image: "04-handshake", tagline: "きっと、仲良くなれる。", synopsis: "言葉がなくても伝わること。小さな柴犬がつなぐ、あたたかな日々。※画面確認用のサンプル作品です。", episodes: (1...3).map { .init(id: $0, title: ["はじめまして", "友だちになろう", "また明日"][$0 - 1], panels: []) })
    ]
}

struct Cover: View {
    let name: String
    var body: some View {
        if let url = Bundle.main.url(forResource: name, withExtension: "png", subdirectory: "Artwork"),
           let image = UIImage(contentsOfFile: url.path) {
            Image(uiImage: image).resizable().scaledToFill()
        } else {
            Rectangle().fill(.orange.opacity(0.15)).overlay { Image(systemName: "book.closed") }
        }
    }
}

struct CatalogView: View {
    @State private var query = ""
    @State private var genre = "すべて"
    private let genres = ["すべて", "ファンタジー", "恋愛", "日常"]
    private var titles: [MangaTitle] {
        Catalog.titles.filter { (genre == "すべて" || $0.genre == genre) && (query.isEmpty || $0.title.localizedCaseInsensitiveContains(query)) }
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
                        Image(systemName: "sparkles").font(.title).foregroundStyle(.orange)
                    }
                    if query.isEmpty && genre == "すべて", let featured = Catalog.titles.first {
                        NavigationLink(value: featured) {
                            ZStack(alignment: .bottomLeading) {
                                Cover(name: featured.image)
                                LinearGradient(colors: [.clear, .black.opacity(0.85)], startPoint: .center, endPoint: .bottom)
                                VStack(alignment: .leading, spacing: 8) {
                                    Text("PICK UP").font(.caption.bold()).padding(.horizontal, 10).padding(.vertical, 5).background(.orange, in: Capsule())
                                    Text(featured.tagline).font(.title2.bold())
                                    Text(featured.title).font(.subheadline.bold())
                                    Text("第1話を無料で読む  →").font(.caption.bold())
                                }.foregroundStyle(.white).padding(20)
                            }.frame(height: 290).clipped().clipShape(RoundedRectangle(cornerRadius: 20))
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
                    if titles.isEmpty {
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
                                    Text("全\(title.episodes.count)話 · 無料").font(.caption).foregroundStyle(.secondary)
                                }
                            }.buttonStyle(.plain)
                        }
                    }
                    Text("オリジナル作品と画面確認用サンプルを掲載しています。").font(.caption2).foregroundStyle(.secondary)
                }.padding(20)
            }
            .background(Color(.systemBackground))
            .toolbar(.hidden, for: .navigationBar)
            .searchable(text: $query, prompt: "作品タイトルで検索")
            .navigationDestination(for: MangaTitle.self) { TitleDetailView(title: $0) }
        }
    }
}

struct TitleDetailView: View {
    let title: MangaTitle
    @State private var descending = false
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
                        Text("全\(title.episodes.count)話 · 全話無料").font(.caption.bold())
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
                Divider()
                HStack {
                    Text("話一覧").font(.title3.bold())
                    Text("\(title.episodes.count)話").font(.caption).foregroundStyle(.secondary)
                    Spacer()
                    Button { descending.toggle() } label: {
                        Label(descending ? "新しい順" : "古い順", systemImage: "arrow.up.arrow.down").font(.caption)
                    }
                }
                VStack(spacing: 0) {
                    ForEach(episodes) { episode in
                        NavigationLink { ReaderView(title: title, episode: episode) } label: {
                            HStack(spacing: 14) {
                                Cover(name: episode.panels.first ?? title.image).frame(width: 70, height: 58).clipped().clipShape(RoundedRectangle(cornerRadius: 8))
                                VStack(alignment: .leading, spacing: 5) {
                                    Text("第\(episode.id)話").font(.caption).foregroundStyle(.secondary)
                                    Text(episode.title).font(.subheadline.bold())
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
    }
}

struct ReaderView: View {
    let title: MangaTitle
    let episode: Episode
    var body: some View {
        ScrollView {
            if episode.panels.isEmpty {
                ContentUnavailableView("サンプルの話です", systemImage: "book.closed", description: Text("この作品は話を選ぶ画面の確認用です。\n「柴犬ポチと魔王の『おて』」第1話は読めます。"))
                    .padding(.top, 80)
            } else {
                LazyVStack(spacing: 32) {
                    VStack(spacing: 12) {
                        Text(title.title).font(.title2.bold())
                        Text("第\(episode.id)話　\(episode.title)").font(.subheadline)
                    }.padding(.vertical, 50).padding(.horizontal)
                    ForEach(episode.panels, id: \.self) { panel in
                        if let url = Bundle.main.url(forResource: panel, withExtension: "png", subdirectory: "Artwork"), let image = UIImage(contentsOfFile: url.path) {
                            Image(uiImage: image).resizable().scaledToFit()
                        }
                    }
                    Text("第\(episode.id)話 おわり").font(.headline).padding(.vertical, 60)
                }
            }
        }.navigationTitle("第\(episode.id)話").navigationBarTitleDisplayMode(.inline)
    }
}

#Preview { CatalogView() }

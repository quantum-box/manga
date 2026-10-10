import Foundation
@main struct ReadingHistoryTests {
    static func main() {
        let suite = "manga-history-tests-" + UUID().uuidString
        let defaults = UserDefaults(suiteName: suite)!
        defer { defaults.removePersistentDomain(forName: suite) }
        var value = ReadingHistory.setting(true, in: "[]", titleID: "online-swordsaint", number: 1)
        value = ReadingHistory.setting(true, in: value, titleID: "online-swordsaint", number: 2)
        defaults.set(value, forKey: ReadingHistory.storageKey)
        let reloaded = UserDefaults(suiteName: suite)!.string(forKey: ReadingHistory.storageKey)!
        precondition(ReadingHistory.contains(reloaded, titleID: "swordsaint", number: 1))
        precondition(ReadingHistory.contains(reloaded, titleID: "online-swordsaint", number: 2))
        precondition(!ReadingHistory.contains(reloaded, titleID: "online-pochi", number: 1))
        precondition(!ReadingHistory.contains(reloaded, titleID: "online-swordsaint", number: 3))
        let removed = ReadingHistory.setting(false, in: reloaded, titleID: "swordsaint", number: 1)
        precondition(!ReadingHistory.contains(removed, titleID: "online-swordsaint", number: 1))
        precondition(ReadingHistory.contains(removed, titleID: "swordsaint", number: 2))
        precondition(!ReadingHistory.contains("invalid-json", titleID: "swordsaint", number: 1))
        print("PASS: history persists across reloads, shares online/offline editions, isolates chapters and series, and resets to unread")
    }
}

pub struct SeriesInfo {
    pub id: String,
    pub title: String,
    pub number: u32,
    pub edition: String,
    pub rank: u32,
}

pub fn identify(id: &str, title: &str) -> SeriesInfo {
    let (series, canonical) = if id.starts_with("swordsaint-") {
        ("swordsaint", "剣聖、仇の弟子に転生する")
    } else if id.starts_with("pochi-") || id == "pochis-handshake" {
        ("pochi", "転生したら柴犬だった。")
    } else if id.starts_with("star-lighthouse-") {
        ("star-lighthouse", "星を拾う夜")
    } else if id.starts_with("lost-property-clerk-") {
        ("lost-property-clerk", "終電後の落とし物係")
    } else if id.starts_with("zero-break-") {
        ("zero-break", "ゼロ・ブレイク")
    } else if id.starts_with("tower-farm-kitchen-") {
        ("tower-farm-kitchen", "塔の農夫は、英雄を食わせる")
    } else if id.starts_with("tower-forge-") {
        ("tower-forge", "塔を灯す剣")
    } else if id.starts_with("star-ring-regalia-") {
        ("star-ring-regalia", "星環のレガリア")
    } else {
        (id, title)
    };
    let number = id
        .split("episode-")
        .nth(1)
        .and_then(|s| s.split('-').next())
        .and_then(|s| s.parse().ok())
        .unwrap_or(1);
    let (edition, rank) = match id {
        "swordsaint-episode-01-white-v3" => ("白背景・ゆっくり版", 0),
        "swordsaint-white-v2" => ("白背景・v2", 1),
        "swordsaint-episode-01-white" => ("白背景・初稿", 2),
        "swordsaint-episode-01" => ("初稿・夜色版", 3),
        "pochi-episode-01" => ("縦読み再構成v2", 0),
        "pochis-handshake" => ("縦読み初稿", 1),
        "pochi-page-v2" => ("白黒ページ・v2", 2),
        "pochi-page-v1" => ("白黒ページ・初稿", 3),
        "star-lighthouse-v1" => ("初稿", 1),
        "zero-break-v5" => ("v5", 0),
        "zero-break-v4" => ("v4", 1),
        "zero-break-v3" => ("v3", 2),
        "zero-break-v3-lettered-sample" => ("v3・文字入り試作", 3),
        "zero-break-v3-vertical-lettered-sample" => ("v3・縦書き試作", 4),
        "zero-break-v2" => ("v2", 5),
        "zero-break-v1" => ("初稿", 6),
        _ => ("", 0),
    };
    SeriesInfo {
        id: series.into(),
        title: canonical.into(),
        number,
        edition: edition.into(),
        rank,
    }
}

pub fn chapter_title<'a>(id: &str, fallback: &'a str) -> &'a str {
    if id.starts_with("zero-break-") && identify(id, fallback).number == 1 {
        "最弱判定、最強の一歩。"
    } else if matches!(
        id,
        "pochi-episode-01" | "pochi-page-v1" | "pochi-page-v2" | "pochis-handshake"
    ) {
        "ポチと魔王の「おて」"
    } else if id == "swordsaint-white-v2" {
        "その手は、二度目"
    } else {
        fallback
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn groups_editions_and_numbers_chapters() {
        for id in ["pochis-handshake", "pochi-episode-01", "pochi-page-v1"] {
            assert_eq!(identify(id, "different title").id, "pochi");
        }
        assert_eq!(identify("swordsaint-white-v2", "").number, 1);
        assert_eq!(identify("swordsaint-episode-10-white", "").number, 10);
        assert_eq!(
            chapter_title("zero-break-v5", "v5"),
            "最弱判定、最強の一歩。"
        );
        assert!(identify("zero-break-v5", "").rank < identify("zero-break-v1", "").rank);
        assert_eq!(
            chapter_title("zero-break-episode-02", "英雄の請求書"),
            "英雄の請求書"
        );
        assert_eq!(
            chapter_title("zero-break-episode-10", "拍手より先に"),
            "拍手より先に"
        );
    }
    #[test]
    fn unrelated_uploads_stay_separate() {
        assert_eq!(identify("new-work", "新作").id, "new-work");
        assert_eq!(identify("new-work", "新作").title, "新作");
    }
    #[test]
    fn tower_forge_uploads_form_one_ten_chapter_series() {
        for number in 1..=10 {
            let id = format!("tower-forge-episode-{number:02}-r123abc");
            let info = identify(&id, "different title");
            assert_eq!(info.id, "tower-forge");
            assert_eq!(info.title, "塔を灯す剣");
            assert_eq!(info.number, number);
            assert_eq!(chapter_title(&id, "chapter subtitle"), "chapter subtitle");
        }
        assert_eq!(identify("tower-forge-other", "").id, "tower-forge");
        assert_eq!(identify("tower-farm-kitchen-episode-01-r123abc", "").id, "tower-farm-kitchen");
    }
    #[test]
    fn revision_ids_keep_series_chapter_numbers_and_new_titles() {
        for (id, expected) in [
            ("pochi-episode-02-r123abc", "pochi"),
            ("zero-break-episode-01-r123abc", "zero-break"),
            ("star-ring-regalia-episode-01-r123abc", "star-ring-regalia"),
        ] {
            assert_eq!(identify(id, "").id, expected);
        }
        assert_eq!(identify("pochi-episode-02-r123abc", "").number, 2);
        assert_eq!(identify("star-ring-regalia-episode-02-r123abc", "").number, 2);
        assert_eq!(identify("star-ring-regalia-episode-01-r123abc", "").title, "星環のレガリア");
        for number in 1..=10 {
            let id = format!("tower-farm-kitchen-episode-{number:02}-r123abc");
            let info = identify(&id, "different title");
            assert_eq!(info.id, "tower-farm-kitchen");
            assert_eq!(info.title, "塔の農夫は、英雄を食わせる");
            assert_eq!(info.number, number);
        }
        assert_eq!(
            chapter_title("pochi-episode-02-r123abc", "言葉のない約束"),
            "言葉のない約束"
        );
        assert_eq!(
            chapter_title("pochi-episode-01-r123abc", "知らない体"),
            "知らない体"
        );
    }
}

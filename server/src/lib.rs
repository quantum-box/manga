use serde::{Deserialize, Serialize};
use worker::*;
mod series;
use std::hash::{Hash, Hasher};

const MAX_IMAGE: usize = 16 * 1024 * 1024;
#[derive(Deserialize, Serialize)]
struct Episode {
    title: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    subtitle: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    cover: Option<String>,
    blocks: Vec<Block>,
}
#[derive(Deserialize, Serialize)]
#[serde(tag = "type", rename_all = "lowercase")]
enum Block {
    Image { src: String, alt: String },
    Caption { text: String },
    Speech { speaker: String, text: String },
    Spacer { size: String },
    Ending { text: String },
}
fn slug(s: &str) -> bool {
    !s.is_empty()
        && s.len() <= 80
        && s.bytes()
            .all(|c| c.is_ascii_alphanumeric() || c == b'-' || c == b'_')
}
fn image_name(s: &str) -> bool {
    s.rsplit_once('.')
        .is_some_and(|(stem, ext)| slug(stem) && matches!(ext, "png" | "jpg" | "webp"))
}
fn headers(content_type: &str, cache: &str) -> Result<Headers> {
    let h = Headers::new();
    h.set("Content-Type", content_type)?;
    h.set("Cache-Control", cache)?;
    h.set("X-Content-Type-Options", "nosniff")?;
    h.set("Content-Security-Policy", "default-src 'self'; img-src 'self'; script-src 'self'; style-src 'self'; frame-ancestors 'none'")?;
    Ok(h)
}
async fn handle(mut req: Request, env: Env) -> Result<Response> {
    let path = req.path();
    if req.method() == Method::Get {
        let asset = match path.as_str() {
            "/" => Some((
                include_str!("../web/index.html"),
                "text/html; charset=utf-8",
            )),
            "/app.js" => Some((
                include_str!("../web/app.js"),
                "text/javascript; charset=utf-8",
            )),
            "/style.css" => Some((include_str!("../web/style.css"), "text/css; charset=utf-8")),
            _ => None,
        };
        if let Some((body, mime)) = asset {
            return Ok(Response::ok(body)?.with_headers(headers(mime, "no-cache")?));
        }
        if path == "/health" {
            return Response::from_json(&serde_json::json!({"status":"ok"}));
        }
    }
    let parts: Vec<_> = path.trim_matches('/').split('/').collect();
    let admin = parts.first() == Some(&"admin");
    if admin {
        let token = env.secret("ADMIN_TOKEN")?.to_string();
        if token.len() < 32
            || req.headers().get("Authorization")?.as_deref() != Some(&format!("Bearer {token}"))
        {
            return Response::error("Unauthorized", 401);
        }
        if req.method() == Method::Put {
            let limit = if parts.get(1) == Some(&"images") {
                MAX_IMAGE
            } else {
                256 * 1024
            };
            let declared = req
                .headers()
                .get("Content-Length")?
                .and_then(|v| v.parse::<usize>().ok());
            if declared.is_none() {
                return Response::error("Content-Length required", 411);
            }
            if declared.unwrap() > limit {
                return Response::error("Too large", 413);
            }
        }
    }
    let bucket = env.bucket("MANGA")?;
    match (req.method(), parts.as_slice()) {
        (Method::Get, ["api", "v1", "catalog"]) => {
            // A publish changes the generation, so a cached index can never hide it indefinitely.
            let generation = bucket
                .head("catalog/generation")
                .await?
                .map(|o| o.etag())
                .unwrap_or_default();
            let mut hasher = std::collections::hash_map::DefaultHasher::new();
            include_str!("../../content/catalog.json").hash(&mut hasher);
            include_str!("series.rs").hash(&mut hasher);
            include_str!("lib.rs").hash(&mut hasher);
            let index_key = format!("catalog/index-v2-{:x}.json", hasher.finish());
            if let Some(index) = bucket.get(&index_key).execute().await? {
                if index.custom_metadata()?.get("generation") == Some(&generation) {
                    let bytes = index.body().ok_or("Missing index body")?.bytes().await?;
                    return Ok(Response::from_bytes(bytes)?
                        .with_headers(headers("application/json", "public, max-age=30")?));
                }
            }
            let metadata: Vec<serde_json::Value> =
                serde_json::from_str(include_str!("../../content/catalog.json"))?;
            let list = bucket
                .list()
                .prefix("episodes/")
                .limit(100)
                .execute()
                .await?;
            let mut groups = std::collections::BTreeMap::<
                String,
                Vec<(series::SeriesInfo, String, String, String, String)>,
            >::new();
            for object in list.objects() {
                let key = object.key();
                let id = key
                    .trim_start_matches("episodes/")
                    .trim_end_matches(".json");
                if !slug(id) {
                    continue;
                }
                let Some(object) = bucket.get(&key).execute().await? else {
                    continue;
                };
                let revision = object.etag();
                let ep: Episode =
                    serde_json::from_slice(&object.body().ok_or("Missing body")?.bytes().await?)?;
                let Some(cover) = ep.cover.as_ref().or_else(|| {
                    ep.blocks.iter().find_map(|b| {
                        if let Block::Image { src, .. } = b {
                            Some(src)
                        } else {
                            None
                        }
                    })
                }) else {
                    continue;
                };
                let info = series::identify(id, &ep.title);
                groups.entry(info.id.clone()).or_default().push((
                    info,
                    id.to_owned(),
                    ep.subtitle.unwrap_or_else(|| ep.title.clone()),
                    format!("/images/{id}/{cover}"),
                    revision,
                ));
            }
            let mut titles = Vec::new();
            for (series_id, mut entries) in groups {
                entries.sort_by(|a, b| {
                    (a.0.number, a.0.rank, &a.1).cmp(&(b.0.number, b.0.rank, &b.1))
                });
                let revisions: Vec<_> = entries.iter().map(|e| e.4.as_str()).collect();
                let revision = revisions.join(":");
                let meta_id = if series_id == "heavenly-demon" {
                    "heavenly-demon-ngplus"
                } else {
                    &series_id
                };
                let meta = metadata.iter().find(|m| m["id"].as_str() == Some(meta_id));
                let episodes: Vec<_> = entries.iter().map(|(info, id, subtitle, _, revision)| {
                    let local_id = id.strip_prefix(&format!("{series_id}-")).unwrap_or(id);
                    let episode_meta = meta.and_then(|m| m["episodes"].as_array()).and_then(|eps| {
                        eps.iter().find(|e| e["id"].as_str() == Some(local_id))
                            .or_else(|| eps.iter().find(|e| e["number"].as_u64() == Some(u64::from(info.number))))
                    });
                    let chapter_title = series::chapter_title(id, episode_meta.and_then(|e| e["title"].as_str()).unwrap_or(subtitle));
                    let edition = episode_meta.and_then(|e| e["edition"].as_str()).unwrap_or(&info.edition);

                    serde_json::json!({
                        "id": id, "number": info.number, "title": chapter_title, "edition": edition,
                        "revision": revision, "reader": format!("/?episode={id}"), "background": "#111111"
                    })
                }).collect();
                titles.push(serde_json::json!({
                    "id": format!("online-{series_id}"), "title": meta.and_then(|m| m["title"].as_str()).unwrap_or(&entries[0].0.title),
                    "genre": meta.and_then(|m| m["genre"].as_str()).unwrap_or("Webtoon"), "revision": revision, "image": entries[0].3,
                    "tagline": meta.and_then(|m| m["tagline"].as_str()).unwrap_or(""),
                    "synopsis": meta.and_then(|m| m["synopsis"].as_str()).unwrap_or("配信中のWebtoon"), "episodes": episodes
                }));
            }
            let bytes = serde_json::to_vec(&titles)?;
            bucket
                .put(index_key, bytes.clone())
                .custom_metadata(std::collections::HashMap::from([(
                    "generation".into(),
                    generation,
                )]))
                .execute()
                .await?;
            Ok(Response::from_bytes(bytes)?
                .with_headers(headers("application/json", "public, max-age=30")?))
        }
        (Method::Get, ["admin", "images", id, name]) if slug(id) && image_name(name) => {
            let Some(obj) = bucket.get(format!("images/{id}/{name}")).execute().await? else {
                return Response::error("Not found", 404);
            };
            let mime = obj
                .http_metadata()
                .content_type
                .unwrap_or("application/octet-stream".into());
            Ok(
                Response::from_stream(obj.body().ok_or("Missing body")?.stream()?)?
                    .with_headers(headers(&mime, "no-store")?),
            )
        }
        (Method::Get, ["api", "episodes"]) => {
            let list = bucket
                .list()
                .prefix("episodes/")
                .limit(1000)
                .execute()
                .await?;
            let ids: Vec<_> = list
                .objects()
                .iter()
                .map(|o| {
                    o.key()
                        .trim_start_matches("episodes/")
                        .trim_end_matches(".json")
                        .to_owned()
                })
                .collect();
            Ok(Response::from_json(&ids)?.with_headers(headers("application/json", "no-store")?))
        }
        (Method::Get, ["api", "episodes", id]) if slug(id) => {
            let Some(obj) = bucket.get(format!("episodes/{id}.json")).execute().await? else {
                return Response::error("Not found", 404);
            };
            let etag = obj.http_etag();
            let bytes = obj.body().ok_or("Missing body")?.bytes().await?;
            let h = headers("application/json", "no-cache")?;
            h.set("ETag", &etag)?;
            Ok(Response::from_bytes(bytes)?.with_headers(h))
        }
        (Method::Get, ["images", id, name]) if slug(id) && image_name(name) => {
            // Only images referenced by a published episode are public.
            let Some(episode) = bucket.get(format!("episodes/{id}.json")).execute().await? else {
                return Response::error("Not found", 404);
            };
            let ep: Episode =
                serde_json::from_slice(&episode.body().ok_or("Missing body")?.bytes().await?)
                    .map_err(|_| Error::from("Invalid stored episode"))?;
            if ep.cover.as_deref() != Some(*name)
                && !ep
                    .blocks
                    .iter()
                    .any(|b| matches!(b, Block::Image { src, .. } if src == name))
            {
                return Response::error("Not found", 404);
            }
            let Some(obj) = bucket.get(format!("images/{id}/{name}")).execute().await? else {
                return Response::error("Not found", 404);
            };
            let mime = obj
                .http_metadata()
                .content_type
                .unwrap_or("application/octet-stream".into());
            Ok(
                Response::from_stream(obj.body().ok_or("Missing body")?.stream()?)?
                    .with_headers(headers(&mime, "public, max-age=300")?),
            )
        }
        (Method::Put, ["admin", "images", id, name]) if slug(id) && image_name(name) => {
            let mime = match name.rsplit('.').next().unwrap_or_default() {
                "png" => "image/png",
                "jpg" => "image/jpeg",
                _ => "image/webp",
            };
            if req.headers().get("Content-Type")?.as_deref() != Some(mime) {
                return Response::error("Invalid Content-Type", 415);
            }
            let bytes = req.bytes().await?;
            if bytes.is_empty() || bytes.len() > MAX_IMAGE {
                return Response::error("Invalid size", 413);
            }
            let valid = match mime {
                "image/png" => bytes.starts_with(b"\x89PNG\r\n\x1a\n"),
                "image/jpeg" => bytes.starts_with(b"\xff\xd8\xff"),
                _ => bytes.len() >= 12 && &bytes[..4] == b"RIFF" && &bytes[8..12] == b"WEBP",
            };
            if !valid {
                return Response::error("Invalid image", 415);
            }
            let key = format!("images/{id}/{name}");
            // Published image names are immutable; upload a new name to replace one.
            let result = bucket
                .put(key, bytes)
                .http_metadata(worker::HttpMetadata {
                    content_type: Some(mime.into()),
                    ..Default::default()
                })
                .only_if(worker::Conditional {
                    etag_does_not_match: Some("*".into()),
                    ..Default::default()
                })
                .execute()
                .await?;
            if result.is_none() {
                return Response::error("Image already exists", 409);
            }
            Response::empty().map(|r| r.with_status(201))
        }
        (Method::Delete, ["admin", "images", id]) if slug(id) => {
            // Published episodes must be withdrawn before their image objects are purged.
            if bucket.head(format!("episodes/{id}.json")).await?.is_some() {
                return Response::error("Unpublish the episode before purging images", 409);
            }
            let prefix = format!("images/{id}/");
            let page = bucket.list().prefix(&prefix).limit(1000).execute().await?;
            let keys: Vec<String> = page.objects().iter().map(|object| object.key()).collect();
            let deleted = keys.len();
            if !keys.is_empty() {
                bucket.delete_multiple(keys).await?;
            }
            // Each call removes the first page, so retries also recover partial deletions.
            let remaining = !bucket
                .list()
                .prefix(&prefix)
                .limit(1)
                .execute()
                .await?
                .objects()
                .is_empty();
            Ok(Response::from_json(
                &serde_json::json!({"deleted": deleted, "remaining": remaining}),
            )?
            .with_headers(headers("application/json", "no-store")?))
        }
        (Method::Delete, ["admin", "episodes", id]) if slug(id) => {
            let key = format!("episodes/{id}.json");
            bucket.delete(&key).await?;
            // R2 ETags are content based. Never reuse a generation, including retries
            // for missing episodes, or an old catalog index could become valid.
            let mutation = format!(
                "{}-{:x}-{:x}",
                Date::now().as_millis(),
                js_sys::Math::random().to_bits(),
                js_sys::Math::random().to_bits()
            );
            bucket
                .put("catalog/generation", format!("deleted-{mutation}-{id}"))
                .execute()
                .await?;
            Response::empty().map(|r| r.with_status(204))
        }
        (Method::Put, ["admin", "episodes", id]) if slug(id) => {
            let bytes = req.bytes().await?;
            if bytes.len() > 256 * 1024 {
                return Response::error("Too large", 413);
            }
            let Ok(ep) = serde_json::from_slice::<Episode>(&bytes) else {
                return Response::error("Invalid episode JSON", 400);
            };
            if ep.title.trim().is_empty()
                || ep.title.len() > 500
                || ep.blocks.is_empty()
                || ep.blocks.len() > 500
            {
                return Response::error("Invalid episode", 400);
            }
            if let Some(cover) = &ep.cover {
                if !image_name(cover)
                    || bucket.head(format!("images/{id}/{cover}")).await?.is_none()
                {
                    return Response::error("Upload a valid cover before publishing", 409);
                }
            }
            let mut images = 0;
            for block in &ep.blocks {
                if let Block::Image { src, .. } = block {
                    if !image_name(src) {
                        return Response::error("Invalid image name", 400);
                    }
                    if bucket.head(format!("images/{id}/{src}")).await?.is_none() {
                        return Response::error("Upload images before publishing", 409);
                    }
                    images += 1;
                }
            }
            if images == 0 {
                return Response::error("An image is required", 400);
            }
            let published = bucket
                .put(format!("episodes/{id}.json"), serde_json::to_vec(&ep)?)
                .execute()
                .await?
                .ok_or("Episode was not stored")?;
            bucket
                .put("catalog/generation", format!("{}-{id}", published.etag()))
                .execute()
                .await?;
            Response::empty().map(|r| r.with_status(204))
        }
        _ => Response::error("Not found", 404),
    }
}
#[event(fetch)]
pub async fn main(req: Request, env: Env, _ctx: Context) -> Result<Response> {
    match handle(req, env).await {
        Ok(response) => Ok(response),
        Err(_) => Response::error("Service unavailable", 503),
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn rejects_path_traversal_and_active_formats() {
        for name in ["../x.png", "x.svg", "x.html", "x/y.png", ".png"] {
            assert!(!image_name(name));
        }
        assert!(image_name("01-rebirth.png"));
        assert!(!slug("../private"));
    }
    #[test]
    fn reads_existing_episode_format() {
        let ep: Episode = serde_json::from_str(include_str!(
            "../../examples/pochis-handshake/webtoon/episode.json"
        ))
        .unwrap();
        let encoded = serde_json::to_value(&ep).unwrap();
        assert_eq!(encoded["subtitle"], "ポチと魔王の、おて。");
        assert_eq!(
            ep.blocks
                .iter()
                .filter(|b| matches!(b, Block::Image { .. }))
                .count(),
            4
        );
    }
}

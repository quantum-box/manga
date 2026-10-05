use serde::{Deserialize, Serialize};
use worker::*;

const MAX_IMAGE: usize = 16 * 1024 * 1024;
#[derive(Deserialize, Serialize)]
struct Episode {
    title: String,
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
            let list = bucket
                .list()
                .prefix("episodes/")
                .limit(100)
                .execute()
                .await?;
            let mut titles = Vec::new();
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
                let ep: Episode =
                    serde_json::from_slice(&object.body().ok_or("Missing body")?.bytes().await?)?;
                let Some(cover) = ep.blocks.iter().find_map(|b| {
                    if let Block::Image { src, .. } = b {
                        Some(src)
                    } else {
                        None
                    }
                }) else {
                    continue;
                };
                titles.push(serde_json::json!({
                    "id": format!("online-{id}"), "title": ep.title, "genre": "Webtoon",
                    "image": format!("/images/{id}/{cover}"), "tagline": ep.title,
                    "synopsis": "配信中のWebtoon", "episodes": [{
                        "id": id, "number": 1, "title": ep.title, "edition": "配信版",
                        "reader": format!("/?episode={id}"), "background": "#111111"
                    }]
                }));
            }
            Ok(
                Response::from_json(&titles)?
                    .with_headers(headers("application/json", "no-store")?),
            )
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
            let bytes = obj.body().ok_or("Missing body")?.bytes().await?;
            Ok(Response::from_bytes(bytes)?.with_headers(headers("application/json", "no-cache")?))
        }
        (Method::Get, ["images", id, name]) if slug(id) && image_name(name) => {
            // Only images referenced by a published episode are public.
            let Some(episode) = bucket.get(format!("episodes/{id}.json")).execute().await? else {
                return Response::error("Not found", 404);
            };
            let ep: Episode =
                serde_json::from_slice(&episode.body().ok_or("Missing body")?.bytes().await?)
                    .map_err(|_| Error::from("Invalid stored episode"))?;
            if !ep
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
            bucket
                .put(format!("episodes/{id}.json"), serde_json::to_vec(&ep)?)
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
        assert_eq!(
            ep.blocks
                .iter()
                .filter(|b| matches!(b, Block::Image { .. }))
                .count(),
            4
        );
    }
}

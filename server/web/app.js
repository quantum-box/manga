const root = document.querySelector('#reader');
function text(tag, value, className) {
  const el = document.createElement(tag); el.textContent = value;
  if (className) el.className = className;
  return el;
}
function link(label, href) {
  const el = text('a', label); el.href = href; return el;
}
function seriesURL(series) { return '/?series=' + encodeURIComponent(series.id); }
function episodeURL(id) { return '/?episode=' + encodeURIComponent(id); }
const historyKey = 'manga.readChapters.v1';
let readChapters = new Set();
function restoreReadChapters() {
  try {
    const saved = JSON.parse(localStorage.getItem(historyKey) || '[]');
    if (Array.isArray(saved)) readChapters = new Set(saved.filter(key => typeof key === 'string'));
  } catch {} // Reading still works when local storage is unavailable.
}
function chapterKey(series, number) { return series.id + ':' + number; }
function isRead(series, number) { return readChapters.has(chapterKey(series, number)); }
function setRead(series, number, read) {
  const key = chapterKey(series, number);
  if (read) readChapters.add(key); else readChapters.delete(key);
  try { localStorage.setItem(historyKey, JSON.stringify([...readChapters])); } catch {}
}
async function json(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('読み込めませんでした。時間をおいて再読み込みしてください。');
  return response.json();
}
async function load() {
  restoreReadChapters();
  const params = new URL(location.href).searchParams;
  const id = params.get('episode');
  const [catalog, ep] = await Promise.all([json('/api/v1/catalog'), id ? json('/api/episodes/' + encodeURIComponent(id)) : Promise.resolve(null)]);
  root.replaceChildren();
  if (!id) {
    const seriesID = params.get('series');
    if (!seriesID) {
      document.title = 'シリーズ一覧 · Manga';
      root.append(text('h1', 'シリーズ一覧'));
      if (!catalog.length) root.append(text('p', '公開されたシリーズはまだありません。'));
      const nav = document.createElement('nav'); nav.className = 'series-list';
      catalog.forEach(series => {
        const a = link('', seriesURL(series)); a.className = 'series-card';
        a.append(text('strong', series.title));
        const count = new Set(series.episodes.map(ep => ep.number)).size;
        a.append(text('span', count + '話 · ' + series.episodes.length + '版'));
        nav.append(a);
      });
      root.append(nav); return;
    }
    const series = catalog.find(series => series.id === seriesID);
    if (!series) throw new Error('シリーズが見つかりません。');
    document.title = series.title + ' · Manga';
    root.append(text('h1', series.title));
    const chapters = new Map();
    series.episodes.forEach(ep => {
      if (!chapters.has(ep.number)) chapters.set(ep.number, []);
      chapters.get(ep.number).push(ep);
    });
    const ordered = [...chapters].sort((a, b) => a[0] - b[0]);
    const unread = ordered.find(([number]) => !isRead(series, number));
    if (unread && ordered.some(([number]) => isRead(series, number))) {
      root.append(link('続きから読む · 第' + unread[0] + '話', episodeURL(unread[1][0].id)));
    }
    const nav = document.createElement('nav'); nav.className = 'chapter-list';
    [...chapters].sort((a, b) => a[0] - b[0]).forEach(([number, editions]) => {
      const section = document.createElement('section');
      section.append(text('h2', '第' + number + '話'));
      section.append(text('span', isRead(series, number) ? '既読' : '未読', 'read-status'));
      const toggle = text('button', isRead(series, number) ? '未読に戻す' : '既読にする');
      toggle.type = 'button';
      toggle.addEventListener('click', () => { setRead(series, number, !isRead(series, number)); load().catch(error => root.replaceChildren(text('p', error.message))); });
      section.append(toggle);
      const preferred = editions[0];
      section.append(link(preferred.title + (preferred.edition ? ' · ' + preferred.edition : ''), episodeURL(preferred.id)));
      if (editions.length > 1) {
        const details = document.createElement('details');
        details.append(text('summary', 'ほかの版（' + (editions.length - 1) + '）'));
        editions.slice(1).forEach(ep => details.append(link(ep.edition || ep.title, episodeURL(ep.id))));
        section.append(details);
      }
      nav.append(section);
    });
    nav.append(link('シリーズ一覧に戻る', '/')); root.append(nav); return;
  }
  const series = catalog.find(series => series.episodes.some(ep => ep.id === id));
  document.title = (series?.title || ep.title) + ' · Manga';
  if (series) {
    const nav = document.createElement('nav'); nav.append(link('‹ ' + series.title + ' · 話一覧', seriesURL(series))); root.append(nav);
  }
  root.append(text('h1', series?.title || ep.title));
  const chapter = series?.episodes.find(chapter => chapter.id === id);
  if (chapter) root.append(text('p', '第' + chapter.number + '話　' + chapter.title));
  else if (ep.subtitle) root.append(text('p', ep.subtitle));
  ep.blocks.forEach((block, index) => {
    if (block.type === 'image') {
      const img = document.createElement('img');
      img.src = '/images/' + encodeURIComponent(id) + '/' + encodeURIComponent(block.src);
      img.alt = block.alt; img.loading = index < 2 ? 'eager' : 'lazy'; img.decoding = 'async';
      root.append(img);
    } else if (block.type === 'spacer') root.append(text('div', '', 'spacer ' + (block.size === 'long' ? 'long' : '')));
    else root.append(text('p', block.type === 'speech' ? block.speaker + '「' + block.text + '」' : block.text, block.type));
  });
  // Record only once the first page actually loads; failed readers remain unread.
  if (series && chapter) {
    const firstImage = root.querySelector('img');
    const mark = () => setRead(series, chapter.number, true);
    if (!firstImage || (firstImage.complete && firstImage.naturalWidth > 0)) mark();
    else firstImage.addEventListener('load', mark, {once: true});
  }
  const nav = document.createElement('nav');
  if (series) {
    const current = series.episodes.find(ep => ep.id === id);
    const next = series.episodes.find(ep => ep.number === current.number + 1);
    if (next) nav.append(link('次の話 · 第' + next.number + '話', episodeURL(next.id)));
    nav.append(link('このシリーズの話一覧に戻る', seriesURL(series)));
  }
  nav.append(link('シリーズ一覧に戻る', '/')); root.append(nav);
}
load().catch(error => root.replaceChildren(text('p', error.message)));

addEventListener("pageshow", event => { if (event.persisted) load().catch(error => root.replaceChildren(text("p", error.message))); });

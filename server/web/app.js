const root = document.querySelector('#reader');
function text(tag, value, className) {
  const el = document.createElement(tag); el.textContent = value;
  if (className) el.className = className;
  return el;
}
async function json(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('読み込めませんでした。時間をおいて再読み込みしてください。');
  return response.json();
}
async function load() {
  const id = new URL(location.href).searchParams.get('episode');
  root.replaceChildren();
  if (!id) {
    root.append(text('h1', 'Webtoon'));
    const ids = await json('/api/episodes');
    if (!ids.length) root.append(text('p', '公開されたエピソードはまだありません。'));
    const nav = document.createElement('nav');
    ids.forEach(id => { const a = text('a', id); a.href = '/?episode=' + encodeURIComponent(id); nav.append(a); });
    root.append(nav); return;
  }
  const ep = await json('/api/episodes/' + encodeURIComponent(id));
  document.title = ep.title + ' · Manga';
  root.append(text('h1', ep.title));
  if (ep.subtitle) root.append(text('p', ep.subtitle));
  ep.blocks.forEach((block, index) => {
    if (block.type === 'image') {
      const img = document.createElement('img');
      img.src = '/images/' + encodeURIComponent(id) + '/' + encodeURIComponent(block.src);
      img.alt = block.alt; img.loading = index < 2 ? 'eager' : 'lazy'; img.decoding = 'async';
      root.append(img);
    } else if (block.type === 'spacer') root.append(text('div', '', 'spacer ' + (block.size === 'long' ? 'long' : '')));
    else root.append(text('p', block.type === 'speech' ? block.speaker + '「' + block.text + '」' : block.text, block.type));
  });
  const back = text('a', '一覧に戻る'); back.href = '/'; const nav = document.createElement('nav'); nav.append(back); root.append(nav);
}
load().catch(error => root.replaceChildren(text('p', error.message)));

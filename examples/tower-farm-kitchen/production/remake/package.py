#!/usr/bin/env python3
"""Keep originals intact; split reviewed panel borders with CSS display windows."""
from pathlib import Path
import base64,hashlib,html,json,struct,sys
BASE=Path(__file__).resolve().parents[2]
DATA=json.loads(Path(__file__).with_name('episodes.json').read_text())
CSS='''*{box-sizing:border-box}html{background:#e9e2d6;color:#312d26;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Kaku Gothic ProN",sans-serif}body{margin:0}main{max-width:720px;margin:auto;background:#fffaf0;container-type:inline-size}header{padding:80px 24px 70px;text-align:center}h1{font-size:clamp(25px,7cqw,42px);line-height:1.5;margin:14px 0}header p,footer{font-size:18px;line-height:1.7}.series-title{font-size:16px;color:#62684b}small{display:block;font-size:15px;color:#6f705d}section{margin:0;padding:0}figure.scene{position:relative;width:100%;height:var(--window-height);margin:0 0 var(--pause);padding:0;overflow:hidden}figure.scene img{display:block;position:absolute;width:100%;height:auto;top:var(--window-top);left:0}footer{text-align:center;padding:60px 24px 80px;line-height:2}a{color:#3a5d41}nav{display:flex;justify-content:center;gap:24px;flex-wrap:wrap}.pause{position:relative;height:var(--pause);margin:0}.sound{position:absolute;top:24%;right:42%;margin:0;font-size:clamp(20px,6cqw,36px);color:#5f6b45;writing-mode:vertical-rl;letter-spacing:.12em}'''
RUNTIME='''<script>window.webtoonReady=(async()=>{const payload=JSON.parse(document.getElementById('native-art-pool').textContent);for(const [id,data] of Object.entries(payload)){const raw=atob(data),bytes=Uint8Array.from(raw,c=>c.charCodeAt(0)),url=URL.createObjectURL(new Blob([bytes],{type:'image/png'}));const images=[...document.querySelectorAll('img[data-art-id="'+id+'"]')];for(const img of images)img.src=url;await Promise.all(images.map(i=>i.decode()));}document.getElementById('native-art-pool').remove();})();</script>'''
OPENING={'id':'00-remake-opening','art':'art/remake-00-opening.png','prompt':'generation/remake-00-opening.prompt.txt','description':'受付の休憩室で目を覚まし、塔の街を歩いて食堂へ戻る。昨日の畑を見る許可を尋ねる。','dialogue':[['コウ・心','夢じゃ、なかった。'],['エルナ','おはよう。眠れた？'],['コウ','少し。昨日の畑、見てもいい？']],'layout':'continuous','pauseAt390':160,'scrollPurpose':'帰れない朝を受け止め、人との再会から畑へ戻る。'}
def package(number):
 ep=next(e for e in DATA if e['number']==number)
 d=BASE/f'episode-{number:02d}'
 config=json.loads(Path(__file__).with_name('windows.json').read_text()) if Path(__file__).with_name('windows.json').exists() else {}
 sources=[]
 if number==2:sources.append(dict(OPENING))
 for i,s in enumerate(ep['scenes']):
  sid=s[5].get('adoptedId',f'{i+1:02d}-{s[0]}')
  sources.append({'id':sid,'art':f'art/{sid}.png','description':s[1],'dialogue':s[2],'layout':s[3],'pauseAt390':s[4],'scrollPurpose':s[5]['scrollPurpose'],'prompt':f'generation/{sid}.prompt.txt'})
 windows=[];groups=[];pool={};sb=[f'# 第{number}話：{ep["title"]} — 全編改稿','',f'時間：{ep["time"]}',f'開始・終了：{ep["change"]}',f'終了状態：{ep["state"]}','', '原画と表示単位を分ける。原画の全文は以下の順序。表示窓は manifest.json の crop と同じで、原画を改変しない。会話は原画内の縦書き。次話の成果を先に描かない。','']
 prompts=[f'# 第{number}話の実行した生成指示','', '方式：組み込み image_gen。人物・場所・縦書きの基準を参照。原画は無加工で保存し、レビュー済みの境界だけ表示窓として分ける。','']
 for source in sources:
  p=d/source['art'];raw=p.read_bytes();w,h=struct.unpack('>II',raw[16:24]);sha=hashlib.sha256(raw).hexdigest()
  source.update(width=w,height=h,sha256=sha)
  pool[source['id']]=base64.b64encode(raw).decode()
  spec=config.get(f'{number}/{source["id"]}',{'cuts':[],'pauses':[]})
  cuts=[0,*spec['cuts'],h]
  if not all(a<b for a,b in zip(cuts,cuts[1:])):raise ValueError(f'Invalid windows: {source["id"]}')
  transcript=' '.join(f'{a}「{b}」' for a,b in source['dialogue'])
  fragments=[]
  for i,(top,end) in enumerate(zip(cuts,cuts[1:])):
   pause=spec.get('pauses',[])[i] if i<len(spec.get('pauses',[])) else source['pauseAt390'] if i==len(cuts)-2 else 24
   sid=source['id']+f'-window-{i+1:02d}'
   assigned=spec.get('dialogueWindows')
   if assigned is not None and len(assigned)!=len(source['dialogue']):raise ValueError('Dialogue window mapping mismatch')
   local_dialogue=[pair for j,pair in enumerate(source['dialogue']) if (assigned[j] if assigned is not None else 0)==i]
   local_transcript=' '.join(f'{who}「{line}」' for who,line in local_dialogue)
   node=dict(source,id=sid,crop={'x':0,'y':top,'width':w,'height':end-top},pauseAt390=pause,sourceId=source['id'],canvasWidthPercent=100,alignment='center',dialogue=local_dialogue)
   windows.append(node)
   # Native image remains unchanged. Container deliberately represents this exact crop.
   local_alt=f'第{number}話「{ep["title"]}」の場面。'+local_transcript
   fragments.append(f'<figure class="scene {source["layout"]}" id="{sid}" data-source="{source["id"]}" data-pacing-purpose="{html.escape(source["scrollPurpose"],quote=True)}" style="--window-height:{(end-top)/w*100:.8f}cqw;--window-top:{-top/w*100:.8f}cqw;--pause:{pause/390*100:.8f}cqw"><img src="{source["art"]}" width="{w}" height="{h}" alt="{html.escape(local_alt,quote=True)}" data-art-id="{source["id"]}"></figure>')
  groups.append('<section>'+''.join(fragments)+'</section>')
  sb += [f'## {source["id"]}',f'見せる情報・接続・カメラ：{source["description"]}',f'スクロールの目的：{source["scrollPurpose"]}',f'表示窓境界（原画y）：{cuts}。各窓の間：{[s["pauseAt390"] for s in windows if s["sourceId"]==source["id"]]}px（390px幅）。','', '| 順 | 話者 | 正確な全文 | 縦列・右から左 |','| --- | --- | --- | --- |']
  sb += [f'| {i+1} | {who} | {line} | '+ ' / '.join(line[x:x+6] for x in range(0,len(line),6))+' |' for i,(who,line) in enumerate(source['dialogue'])]
  sb += ['','伏せる情報：後続原画と次話の出来事。発話・反応・道具の数と人物の状態は review と validation.json に残す。','']
  pp=d/source.get('prompt','../../production/remake/02-01-opening.prompt.txt')
  if source['id']==OPENING['id']:pp=d/'generation/remake-00-opening.prompt.txt'
  prompts += [f'## {source["id"]}','```text',pp.read_text(),'```','']
 prev=f'<a href="../episode-{number-1:02d}/index.html">前の話</a>'
 nxt=f'<a href="../episode-{number+1:02d}/index.html">次の話</a>' if number<10 else ''
 doc=f'<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第{number}話 {html.escape(ep["title"])}｜塔の農夫は、英雄を食わせる</title><link rel="stylesheet" href="reader.css"></head><body><main><header><span class="series-title">塔の農夫は、英雄を食わせる</span><p>第{number}話</p><h1>{html.escape(ep["title"])}</h1><small>{html.escape(ep["time"])}</small></header>'+''.join(groups)+f'<footer><p>第{number}話 おわり</p><nav>{prev}<a class="series-index" href="../chapters.html">話一覧</a>{nxt}</nav></footer></main><script>if(window.webkit?.messageHandlers?.mangaReader)document.querySelector(".series-index")?.remove();</script></body></html>'
 (d/'reader.css').write_text(CSS+'\n');(d/'index.html').write_text(doc+'\n')
 # Every source is embedded once even when several windows display the same original.
 reader=doc.replace('<link rel="stylesheet" href="reader.css">','<style>'+CSS+'</style>')
 for source in sources:reader=reader.replace('src="'+source['art']+'" ','')
 reader=reader.replace('</body>','<script id="native-art-pool" type="application/json">'+json.dumps(pool,separators=(',',':'))+'</script>'+RUNTIME+'</body>')
 (d/'reader.html').write_text(reader+'\n')
 if (d/'reader.html').stat().st_size>=100*1024*1024:raise ValueError('Standalone reader exceeds GitHub file size')
 (d/'manifest.json').write_text(json.dumps({'number':number,'title':ep['title'],'time':ep['time'],'change':ep['change'],'state':ep['state'],'revision':'2026-10-07-following-remake','sources':sources,'scenes':windows},ensure_ascii=False,indent=2)+'\n')
 (d/'storyboard.md').write_text('\n'.join(sb).rstrip()+'\n');(d/'PROMPTS.md').write_text('\n'.join(prompts).rstrip()+'\n')
 (d/'README.md').write_text(f'# 第{number}話：{ep["title"]}\n\n[読む](index.html) / [単独リーダー](reader.html) / [絵コンテ](storyboard.md) / [生成指示](PROMPTS.md)\n\n全編改稿。{len(sources)}枚の無加工原画を{len(windows)}の表示窓で読み、手順・会話・反応に異なる間を置く。原画と縦書きの会話を組み込みimage_genで一体生成。検証状態は[validation.json](validation.json)。\n')
 print(f'Packaged episode {number}: {len(sources)} originals, {len(windows)} windows')
if __name__=='__main__':
 for n in sys.argv[1:]:package(int(n))

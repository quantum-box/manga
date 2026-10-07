// Native layout only: unmodified source PNGs, the reader's exact display windows.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {createCanvas,loadImage}=require('@napi-rs/canvas');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
module.exports=async function(dir,m){
  const layout=m.scrollLayout,review=path.join(dir,'review');fs.mkdirSync(review,{recursive:true});
  const sources=layout.sources,images=new Map();
  for(const s of sources)images.set(s.id,await loadImage(path.join(dir,'art',s.file)));
  const sourceHashes=sources.map(s=>({id:s.id,file:s.file,sha256:hash(path.join(dir,'art',s.file))}));
  const exports=[],reviewArtifacts=[];
  const write=(file,canvas)=>{fs.writeFileSync(path.join(dir,file),canvas.toBuffer('image/png'));return {file,width:canvas.width,height:canvas.height,sha256:hash(path.join(dir,file))};};
  const draw=(ctx,u,x,y,w,h)=>ctx.drawImage(images.get(u.sourceId),...u.crop,x,y,w,h);
  for(const width of [360,390]){
    const scale=width/390,head=210*scale,foot=130*scale;let y=head;const positions=[];
    for(const u of layout.units){
      const w=width*u.widthPercent/100,h=u.crop[3]*w/u.crop[2];
      const x=u.align==='right'?width-w:u.align==='center'?(width-w)/2:0;
      positions.push({id:u.id,sourceId:u.sourceId,crop:u.crop,x,y,width:w,height:h,pause:u.pause*scale});
      y+=h+u.pause*scale;
    }
    const c=createCanvas(width,Math.ceil(y+foot)),ctx=c.getContext('2d');
    ctx.fillStyle='#ffffff';ctx.fillRect(0,0,width,c.height);
    ctx.fillStyle='#111a29';ctx.fillRect(0,0,width,head);
    ctx.fillStyle='#acd7ee';ctx.font=12*scale+'px sans-serif';ctx.fillText('異世界転生 × スーパーヒーロー / 第1話',24*scale,55*scale);
    ctx.fillStyle='#eef8ff';ctx.font='bold '+32*scale+'px sans-serif';ctx.fillText('ゼロ・ブレイク',24*scale,110*scale);
    ctx.font=15*scale+'px sans-serif';ctx.fillText(m.title,24*scale,160*scale);
    positions.forEach((p,i)=>draw(ctx,layout.units[i],p.x,p.y,p.width,p.height));
    ctx.fillStyle='#203045';ctx.font=15*scale+'px sans-serif';ctx.fillText('第1話 おわり',width/2-45*scale,y+45*scale);
    exports.push({...write('complete-'+width+'.png',c),positions});
    for(let offset=0;offset<positions.length;offset+=6){
      const part=positions.slice(offset,offset+6),board=createCanvas(width*part.length,Math.ceil(Math.max(...part.map(p=>p.height)))+55),b=board.getContext('2d');
      b.fillStyle='#ffffff';b.fillRect(0,0,board.width,board.height);
      part.forEach((p,k)=>{b.fillStyle='#203045';b.font='11px sans-serif';b.fillText(p.id,k*width+6,19);draw(b,layout.units[offset+k],k*width+p.x,40,p.width,p.height);});
      reviewArtifacts.push(write('review/scroll-units-'+width+'-'+String(offset/6).padStart(2,'0')+'.png',board));
    }
    for(const id of ['waiting-voice','waiting-device','result','despair-voice','distant-tremor','decision-voice','armor-click','connection-voice','connection-light','hero','fragment-pickup','fragment-emblem']){
      const p=positions.find(p=>p.id===id),height=width===390?844:800;
      const top=Math.min(Math.max(0,p.y-40*scale),c.height-height);
      const window=createCanvas(width,height),v=window.getContext('2d');v.drawImage(c,0,top,width,height,0,0,width,height);
      reviewArtifacts.push({...write('review/scroll-window-'+width+'-'+id+'.png',window),top});
    }
    // Full-width sequence extract for sharing; this is a native export, not a screenshot.
    const first=positions.find(p=>p.id==='armor-route'),last=positions.find(p=>p.id==='hero');
    const excerpt=createCanvas(width,Math.ceil(last.y+last.height-first.y)),e=excerpt.getContext('2d');
    e.drawImage(c,0,first.y,width,excerpt.height,0,0,width,excerpt.height);
    reviewArtifacts.push(write('review/scroll-armor-sequence-'+width+'.png',excerpt));
  }
  sourceHashes.forEach(s=>{if(hash(path.join(dir,'art',s.file))!==s.sha256)throw Error('Source altered '+s.id);});
  fs.writeFileSync(path.join(dir,'raster-export-validation.json'),JSON.stringify({
    edition:m.scrollEdition,status:'passed_export',method:'native canvas layout from scrollLayout; same source windows and continuous geometry as reader; no HTML or browser rendering',
    sourceArtworkUnchanged:true,sourceHashes,exports,reviewArtifacts,browserPixelsCompared:false,visualReview:'pending'
  },null,2)+'\n');
  fs.writeFileSync(path.join(review,'README.md'),'# 第1話・余白とスクロールの確認\n\nscroll-units-* は360/390px幅の全表示窓。scroll-window-* は全編書き出しから切り出したスマホ寸法の連続窓。scroll-armor-sequence-* は音・通知・光から全身披露までの抜粋。ブラウザの撮影・DOM検査・実機の証明ではない。\n');
  console.log('Episode 1: '+layout.units.length+' display beats, '+sources.length+' unique source PNGs; full native exports at 360/390px');
};

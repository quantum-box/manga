// Native raster layout export; no HTML renderer or browser.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {createCanvas,loadImage}=require('@napi-rs/canvas');
const root=path.resolve(__dirname,'..');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
(async()=>{
for(const n of (process.argv.length>2?process.argv.slice(2).map(Number):Array.from({length:10},(_,i)=>i+1))){
 const dir=path.join(root,n===1?'v5':'episode-'+String(n).padStart(2,'0'));
 const m=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json')));
 if(m.version!=='context-dialogue-v6')throw Error('Expected adopted v6 manifest');
 const review=path.join(dir,'review');fs.mkdirSync(review,{recursive:true});
 const sourceHashes=m.shots.map(s=>({id:s.id,file:s.file,sha256:hash(path.join(dir,'art',s.file))}));
 const images=await Promise.all(m.shots.map(s=>loadImage(path.join(dir,'art',s.file))));
 const exports=[];
 for(const width of [360,390]){
   const unit=width/390,head=Math.round(210*unit),foot=Math.round(130*unit);
   const positions=[];let y=head;
   for(let i=0;i<images.length;i++){
     const s=m.shots[i],im=images[i],w=width*(s.widthPercent||100)/100,h=Math.round(im.height*w/im.width);
     const x=s.shape==='right'?width-w:s.shape==='wide'?(width-w)/2:0;
     positions.push({id:s.id,x,y,width:w,height:h,pause:Math.round(s.pause*unit)});
     y+=h+Math.round(s.pause*unit);
   }
   const c=createCanvas(width,y+foot),ctx=c.getContext('2d');
   ctx.fillStyle=[4,9].includes(n)?'#fffaf3':n===5?'#f6f7f8':'#ffffff';ctx.fillRect(0,0,width,c.height);
   ctx.fillStyle='#111a29';ctx.fillRect(0,0,width,head);
   ctx.fillStyle='#acd7ee';ctx.font=12*unit+'px sans-serif';ctx.fillText('異世界転生 × スーパーヒーロー / 第'+n+'話',24*unit,55*unit);
   ctx.fillStyle='#eef8ff';ctx.font='bold '+32*unit+'px sans-serif';ctx.fillText('ゼロ・ブレイク',24*unit,110*unit);
   ctx.font=15*unit+'px sans-serif';ctx.fillText(m.title||'最弱判定、最強の一歩。',24*unit,160*unit);
   positions.forEach((p,i)=>ctx.drawImage(images[i],p.x,p.y,p.width,p.height));
   ctx.fillStyle='#203045';ctx.font=15*unit+'px sans-serif';ctx.fillText('第'+n+'話 おわり',width/2-45*unit,y+55*unit);
   const out=path.join(dir,'complete-'+width+'.png');fs.writeFileSync(out,c.toBuffer('image/png'));
   exports.push({width,height:c.height,file:path.basename(out),sha256:hash(out),positions});
   // Contact columns keep the exact target display width. Source artwork is not repainted.
   for(let offset=0;offset<images.length;offset+=4){
     const part=positions.slice(offset,offset+4),height=Math.max(...part.map(p=>p.height))+70;
     const board=createCanvas(width*part.length,height),b=board.getContext('2d');
     b.fillStyle='#ffffff';b.fillRect(0,0,board.width,board.height);
     part.forEach((p,k)=>{
       b.fillStyle='#203045';b.font='12px sans-serif';b.fillText(p.id,k*width+8,20);
       b.drawImage(images[offset+k],k*width+p.x,40,p.width,p.height);
     });
     fs.writeFileSync(path.join(review,'v6-contact-'+width+'-'+offset/4+'.png'),board.toBuffer('image/png'));
   }
   for(let i=0;i<positions.length;i++){
     const p=positions[i],height=width===390?844:800;
     const top=Math.min(Math.max(0,p.y+p.height-height/2),c.height-height);
     const viewport=createCanvas(width,height),v=viewport.getContext('2d');
     v.drawImage(c,0,top,width,height,0,0,width,height);
     fs.writeFileSync(path.join(review,'v6-flow-'+width+'-'+String(i).padStart(2,'0')+'.png'),viewport.toBuffer('image/png'));
   }
 }
 sourceHashes.forEach(s=>{if(hash(path.join(dir,'art',s.file))!==s.sha256)throw Error('Source altered');});
 fs.writeFileSync(path.join(dir,'raster-export-validation.json'),JSON.stringify({
   edition:m.version,status:'passed_export',method:'native canvas layout from manifest; no HTML or browser rendering',
   sourceArtworkUnchanged:true,sourceHashes,exports,browserPixelsCompared:false,visualReview:'pending'
 },null,2)+'\n');
 fs.writeFileSync(path.join(review,'README.md'),'# 画像確認\n\nv6-contact-* は各画像を360/390px幅で並べたネイティブ画像書き出し。v6-flow-* は同じ全長画像の連続窓。ブラウザのDOM・画面撮影・実機の証明ではない。\n\n接頭辞v6のない画像は前の縦書き版の検査資料。現在の版の確認には使わない。\n');
 console.log('Episode '+n+': '+m.shots.length+' images; native exports at 360 and 390 px');
}
})().catch(e=>{console.error(e);process.exitCode=1;});

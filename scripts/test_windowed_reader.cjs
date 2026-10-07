// Run the actual inline reader with a small DOM adapter, without opening a browser.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('node:assert/strict');
const {test}=require('node:test');
const dir=path.join(__dirname,'../examples/zero-break/v5');
const html=fs.readFileSync(path.join(dir,'index.html'),'utf8');
const manifest=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json')));
const script=html.match(/<script>\n([\s\S]*?)\n<\/script>/)[1];
function adapter(fail=false){
  const calls=[],decoded=[],released=[];
  const sources=manifest.scrollLayout.sources.map(s=>({id:'source-'+s.id,
    async decode(){if(fail)throw Error('Missing image');decoded.push(s.id);},
    removeAttribute(name){assert.equal(name,'src');released.push(s.id);}}));
  const canvases=[...html.matchAll(/<canvas([^>]+)>/g)].map(match=>{
    const attrs=Object.fromEntries([...match[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(m=>[m[1],m[2]]));
    return {width:Number(attrs.width),height:Number(attrs.height),dataset:{source:attrs['data-source'],crop:attrs['data-crop']},
      getContext(kind){assert.equal(kind,'2d');return {drawImage(...args){calls.push(args);}};}};
  });
  const state={dataset:{}},error={hidden:true},pool={removed:false,remove(){this.removed=true;}};
  return {calls,decoded,released,canvases,state,error,pool,document:{documentElement:state,
    querySelectorAll(selector){return selector==='#artwork-pool img'?sources:canvases;},
    getElementById(id){return id==='artwork-pool'?pool:error;}}};
}
test('standalone reader draws all 76 staged windows from 40 decoded sources, including shared rows',async()=>{
  const dom=adapter();await vm.runInNewContext(script,{document:dom.document});
  assert.equal(dom.calls.length,manifest.scrollLayout.units.length);
  assert.equal(dom.decoded.length,manifest.scrollLayout.sources.length);
  assert.deepEqual(dom.released,dom.decoded);assert.equal(dom.pool.removed,true);
  assert.equal(dom.state.dataset.readerReady,'true');assert.equal(dom.error.hidden,true);
  for(const unit of manifest.scrollLayout.units){
    const matches=dom.calls.filter(args=>args[0].id==='source-'+unit.sourceId && args.slice(1,5).join(',')===unit.crop.join(','));
    assert.equal(matches.length,1,unit.id+' should draw its intended window exactly once');
  }
});
test('missing source shows an actionable error instead of claiming the chapter is rendered',async()=>{
  const dom=adapter(true);await vm.runInNewContext(script,{document:dom.document});
  assert.equal(dom.state.dataset.readerReady,'error');assert.equal(dom.error.hidden,false);
  assert.equal(dom.calls.length,0);assert.equal(dom.pool.removed,false);
});

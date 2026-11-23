/* Mom's Recipe Box — shared script for every page */
(function(){
const store={get(k,d){try{const v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return d}},
             set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const toastEl=$("#toast");let toastT;
function toast(msg){toastEl.textContent=msg;toastEl.classList.add("on");clearTimeout(toastT);toastT=setTimeout(()=>toastEl.classList.remove("on"),3200)}

/* ---------- large text ---------- */
const bigBtn=$("#bigBtn");let big=store.get("big",false);
function applyBig(){document.body.classList.toggle("big",big);bigBtn.setAttribute("aria-pressed",big)}
bigBtn.onclick=()=>{big=!big;store.set("big",big);applyBig()};applyBig();

/* ---------- favorites (shared, via Supabase) ---------- */
const F=window.FAV||{};const H={apikey:F.key};
let favs=new Set(store.get("favs",[]));
function paintFavs(){
  $$(".fav[data-id]").forEach(b=>{const on=favs.has(b.dataset.id);b.setAttribute("aria-pressed",on);
    b.setAttribute("aria-label",on?"Remove from favorites":"Add to favorites")});
  const fg=$("#favgrid");
  if(fg){fg.innerHTML="";
    $$("#grid .tile").forEach(t=>{if(favs.has(t.dataset.id)){const c=t.cloneNode(true);c.hidden=false;fg.appendChild(c)}});
    $("#favempty").hidden=fg.children.length>0}
}
async function loadFavs(){
  try{const r=await fetch(F.url+"?select=recipe_id",{headers:H,cache:"no-store"});if(!r.ok)throw 0;
    const rows=await r.json();favs=new Set(rows.map(x=>x.recipe_id));store.set("favs",[...favs]);paintFavs()}catch(e){}
}
async function toggleFav(id){
  const on=!favs.has(id);on?favs.add(id):favs.delete(id);store.set("favs",[...favs]);paintFavs();
  try{
    const r=on?await fetch(F.url,{method:"POST",headers:{...H,"Content-Type":"application/json","Prefer":"resolution=ignore-duplicates,return=minimal"},body:JSON.stringify([{recipe_id:id}])})
              :await fetch(F.url+"?recipe_id=eq."+encodeURIComponent(id),{method:"DELETE",headers:{...H,"Prefer":"return=minimal"}});
    if(!r.ok){let c="";try{c=(await r.json()).code||""}catch(_){}throw new Error("error "+r.status+(c?" / "+c:""))}
  }catch(e){on?favs.delete(id):favs.add(id);store.set("favs",[...favs]);paintFavs();
    toast("Couldn't save the favorite ("+(e&&e.message?e.message:"no connection")+"). Try again in a moment.")}
}
document.addEventListener("click",e=>{const b=e.target.closest(".fav[data-id]");if(!b)return;e.preventDefault();e.stopPropagation();toggleFav(b.dataset.id)});
document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible")loadFavs()});

/* ---------- home: search + category filter ---------- */
const grid=$("#grid");
if(grid){
  let cat="All";const q=$("#q");
  const run=()=>{let shown=0;const t=q.value.trim().toLowerCase();
    $$(".tile",grid).forEach(el=>{const ok=(cat==="All"||el.dataset.cat===cat)&&(!t||el.dataset.words.includes(t));el.hidden=!ok;if(ok)shown++});
    $("#none").hidden=shown>0};
  q.oninput=run;
  $$("[data-filter]").forEach(b=>b.onclick=()=>{cat=b.dataset.filter;$$("[data-filter]").forEach(x=>x.setAttribute("aria-pressed",x===b));run()});
}
paintFavs();loadFavs();

/* ---------- amounts: scale + units ---------- */
const FR=[[0,""],[1/8,"⅛"],[1/4,"¼"],[1/3,"⅓"],[3/8,"⅜"],[1/2,"½"],[5/8,"⅝"],[2/3,"⅔"],[3/4,"¾"],[7/8,"⅞"],[1,""]];
const PL={cup:"cups",can:"cans",cube:"cubes",package:"packages",loaf:"loaves",handful:"handfuls",bunch:"bunches",strip:"strips",jar:"jars",square:"squares",bag:"bags","small bottle":"small bottles",pint:"pints",tub:"tubs",carton:"cartons",glass:"glasses",pinch:"pinches",slice:"slices",stick:"sticks"};
function frac(x){let w=Math.floor(x+1e-9),r=x-w,b=FR[0];for(const f of FR)if(Math.abs(f[0]-r)<Math.abs(b[0]-r))b=f;if(b[0]===1)w++;return ((w?String(w):"")+b[1])||"0"}
function metricAmt(x,unit){
  if(unit==="g"){const r=x<20?Math.round(x):x<200?Math.round(x/5)*5:Math.round(x/10)*10;return r>=1000?(r/1000).toFixed(1).replace(/\.0$/,"")+" kg":r+" g"}
  const r=x<20?Math.round(x):x<200?Math.round(x/5)*5:Math.round(x/10)*10;return r>=1000?(r/1000).toFixed(1).replace(/\.0$/,"")+" l":r+" ml"}
function metricOf(q,u,gpc,ge){
  if(ge)return [q*ge,"g"];
  if(u==="cup")return gpc?[q*gpc,"g"]:[q*236.6,"ml"];
  if(u==="oz")return [q*28.35,"g"];
  if(u==="lb")return [q*453.6,"g"];
  return null}
function amount(q,q2,u,gpc,ge,metric){
  if(metric){const a=metricOf(q,u,gpc,ge);
    if(a){if(!q2)return metricAmt(a[0],a[1]);const b=metricOf(q2,u,gpc,ge);
      return metricAmt(a[0],a[1]).replace(/ \S+$/,"")+"–"+metricAmt(b[0],b[1])}}
  const top=q2||q,un=u?(top>1+1e-9?(PL[u]||u):u):"";
  return (frac(q)+(q2?"–"+frac(q2):"")+(un?" "+un:"")).trim()
}
let units=store.get("units","us"),scale=1;
function renderAmounts(root=document){
  const metric=units==="metric";document.body.classList.toggle("metric",metric);
  $$(".q[data-q]",root).forEach(s=>{const d=s.dataset;s.textContent=amount(+d.q*scale,d.q2?+d.q2*scale:0,d.u||"",+d.gpc||0,+d.ge||0,metric);s.classList.toggle("scaled",scale!==1)});
  $$(".temp",root).forEach(s=>{const f=+s.dataset.f;s.textContent=metric?Math.round((f-32)*5/9/10)*10+"°C":f+"°F"});
  $$(".fq",root).forEach(s=>{const n=+s.dataset.q*scale,w=s.dataset.w;s.textContent=(frac(n)+" "+(n<=1?w.replace(/s$/,""):w)).trim()});
  $$("#scale button").forEach(b=>b.setAttribute("aria-pressed",+b.dataset.m===scale));
  $$("#units button").forEach(b=>b.setAttribute("aria-pressed",b.dataset.units===units));
}

/* ---------- recipe page ---------- */
const art=$("[data-recipe]");
if(art){
  const id=art.dataset.recipe;const checked=store.get("chk-"+id,{});const done=store.get("stp-"+id,{});
  $$("ul.ing input",art).forEach(c=>{c.checked=!!checked[c.dataset.k];
    c.onchange=()=>{checked[c.dataset.k]=c.checked;store.set("chk-"+id,checked)}});
  $$("ol.steps li",art).forEach(li=>{const i=li.dataset.i;li.classList.toggle("done",!!done[i]);
    li.onclick=e=>{if(e.target.closest(".tbtn"))return;done[i]=!done[i];li.classList.toggle("done",done[i]);store.set("stp-"+id,done)}});
  $("#clr").onclick=()=>{store.set("chk-"+id,{});store.set("stp-"+id,{});location.reload()};
  $$("#scale button").forEach(b=>b.onclick=()=>{scale=+b.dataset.m;renderAmounts()});
  $$("#units button").forEach(b=>b.onclick=()=>{units=b.dataset.units;store.set("units",units);renderAmounts()});
  renderAmounts();
  const lb=$("#lb");lb.onclick=()=>lb.classList.remove("on");
  $$(".cardimg",art).forEach(im=>im.onclick=()=>{lb.querySelector("img").src=im.src;lb.classList.add("on")});
  let lock=null;const wake=async()=>{try{lock=await navigator.wakeLock.request("screen")}catch(e){}};
  if("wakeLock" in navigator){wake();document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible")wake()})}

  /* cook mode: ingredients first, then one step per screen */
  const data=JSON.parse($("#cookdata").textContent),ck=$("#cook");let idx=0;
  const slides=1+data.steps.length;
  function ingHTML(){let h="";$$("#ingcol > h3, #ingcol > ul").forEach(el=>{
    if(el.tagName==="H3")h+=`<h4>${esc(el.textContent)}</h4>`;
    else h+='<ul class="ing">'+$$("li",el).map(li=>{const c=$("input",li);
      return `<li><label><input type="checkbox" data-k="${c.dataset.k}"${c.checked?" checked":""}><span>${$("label > span",li).innerHTML}</span></label></li>`}).join("")+"</ul>"});return h}
  function show(){
    const s=idx===0?null:data.steps[idx-1];
    ck.innerHTML=`<div class="ck-top"><div><div class="ck-title">${esc(data.title)}</div><div class="ck-count">${idx===0?"Ingredients":"Step "+idx+" of "+data.steps.length}</div></div>
      <button class="ck-close">Close</button></div>
      <div class="ck-main">${idx===0?`<h3>Ingredients</h3>${ingHTML()}`:`<div class="ck-step">${s.h}</div>${s.t?`<div><button class="tbtn" data-t="${s.t}">⏱ Start ${s.t}-min timer</button></div>`:""}`}</div>
      <div class="ck-dots">${Array.from({length:slides},(_,i)=>`<i class="${i===idx?"on":""}"></i>`).join("")}</div>
      <div class="ck-bot">${idx>0?'<button class="prev">← Back</button>':""}<button class="next">${idx===slides-1?"Done":idx===0?"Start cooking →":"Next →"}</button></div>`;
    renderAmounts(ck);
    $$("ul.ing input",ck).forEach(c=>c.onchange=()=>{const pg=$(`#ingcol input[data-k="${c.dataset.k}"]`);pg.checked=c.checked;pg.onchange()});
    $(".ck-close",ck).onclick=close;
    const p=$(".prev",ck);if(p)p.onclick=()=>go(-1);
    $(".next",ck).onclick=()=>idx===slides-1?close():go(1);
    const t=$(".tbtn",ck);if(t)t.onclick=()=>startTimer(+t.dataset.t,data.title+" · step "+idx);
  }
  function go(d){idx=Math.max(0,Math.min(slides-1,idx+d));show()}
  function open(){idx=0;ck.hidden=false;document.body.style.overflow="hidden";show()}
  function close(){ck.hidden=true;document.body.style.overflow=""}
  $("#cookBtn").onclick=open;
  document.addEventListener("keydown",e=>{if(ck.hidden)return;if(e.key==="ArrowRight")go(1);else if(e.key==="ArrowLeft")go(-1);else if(e.key==="Escape")close()});
  let x0=null;ck.addEventListener("touchstart",e=>{x0=e.touches[0].clientX},{passive:true});
  ck.addEventListener("touchend",e=>{if(x0==null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>60)go(dx<0?1:-1);x0=null});

  $$(".tbtn",art).forEach(b=>b.onclick=()=>startTimer(+b.dataset.t,b.dataset.l));
}

/* ---------- timers ---------- */
const timersEl=$("#timers");let actx=null;
function beep(){try{if(!actx)return;const o=actx.createOscillator(),g=actx.createGain();o.frequency.value=880;o.connect(g);g.connect(actx.destination);
  g.gain.setValueAtTime(.0001,actx.currentTime);g.gain.exponentialRampToValueAtTime(.3,actx.currentTime+.02);
  g.gain.exponentialRampToValueAtTime(.0001,actx.currentTime+.5);o.start();o.stop(actx.currentTime+.55)}catch(e){}}
function startTimer(min,label){
  try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();actx.resume()}catch(e){}
  let end=Date.now()+min*60000,ring=null;
  const el=document.createElement("div");el.className="timer";
  el.innerHTML=`<div><div class="lbl">${esc(label)}</div><div class="t"></div></div><button>+1 min</button><button aria-label="Close timer">✕</button>`;
  timersEl.appendChild(el);const [plus,close]=$$("button",el);
  plus.onclick=()=>{end=Math.max(end,Date.now())+60000;el.classList.remove("ring");clearInterval(ring);ring=null};
  close.onclick=()=>{clearInterval(iv);clearInterval(ring);el.remove()};
  const tick=()=>{const s=Math.max(0,Math.round((end-Date.now())/1000));
    $(".t",el).textContent=s?`${Math.floor(s/60)}:${String(s%60).padStart(2,"0")}`:"Done!";
    if(s===0&&!ring){el.classList.add("ring");beep();ring=setInterval(beep,1500)}};
  tick();const iv=setInterval(tick,500);
}
})();

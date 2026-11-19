/* Mom's Recipe Box — shared script for every page */
(function(){
const store={get(k,d){try{const v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return d}},
             set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};

/* large text */
const bigBtn=document.getElementById("bigBtn");let big=store.get("big",false);
function applyBig(){document.body.classList.toggle("big",big);bigBtn.setAttribute("aria-pressed",big)}
bigBtn.onclick=()=>{big=!big;store.set("big",big);applyBig()};applyBig();

/* home: search + category filter */
const grid=document.getElementById("grid");
if(grid){
  let cat="All";const q=document.getElementById("q");
  const run=()=>{let shown=0;const t=q.value.trim().toLowerCase();
    grid.querySelectorAll(".tile").forEach(el=>{const ok=(cat==="All"||el.dataset.cat===cat)&&(!t||el.dataset.words.includes(t));el.hidden=!ok;if(ok)shown++});
    document.getElementById("none").hidden=shown>0};
  q.oninput=run;
  document.querySelectorAll("[data-filter]").forEach(b=>b.onclick=()=>{cat=b.dataset.filter;
    document.querySelectorAll("[data-filter]").forEach(x=>x.setAttribute("aria-pressed",x===b));run()});
}

/* recipe page: checklist, steps, timers, card zoom */
const art=document.querySelector("[data-recipe]");
if(art){
  const id=art.dataset.recipe;const checked=store.get("chk-"+id,{});const done=store.get("stp-"+id,{});
  art.querySelectorAll("ul.ing input").forEach(c=>{c.checked=!!checked[c.dataset.k];
    c.onchange=()=>{checked[c.dataset.k]=c.checked;store.set("chk-"+id,checked)}});
  art.querySelectorAll("ol.steps li").forEach(li=>{const i=li.dataset.i;li.classList.toggle("done",!!done[i]);
    li.onclick=e=>{if(e.target.closest(".tbtn"))return;done[i]=!done[i];li.classList.toggle("done",done[i]);store.set("stp-"+id,done)}});
  document.getElementById("clr").onclick=()=>{store.set("chk-"+id,{});store.set("stp-"+id,{});location.reload()};
  art.querySelectorAll(".tbtn").forEach(b=>b.onclick=()=>startTimer(+b.dataset.t,b.dataset.l));
  const lb=document.getElementById("lb");lb.onclick=()=>lb.classList.remove("on");
  art.querySelectorAll(".cardimg").forEach(im=>im.onclick=()=>{lb.querySelector("img").src=im.src;lb.classList.add("on")});
  /* keep the screen awake while a recipe is open (where supported) */
  let lock=null;const wake=async()=>{try{lock=await navigator.wakeLock.request("screen")}catch(e){}};
  if("wakeLock" in navigator){wake();document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible")wake()})}
}

const timersEl=document.getElementById("timers");let actx=null;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function beep(){try{if(!actx)return;const o=actx.createOscillator(),g=actx.createGain();o.frequency.value=880;o.connect(g);g.connect(actx.destination);
  g.gain.setValueAtTime(.0001,actx.currentTime);g.gain.exponentialRampToValueAtTime(.3,actx.currentTime+.02);
  g.gain.exponentialRampToValueAtTime(.0001,actx.currentTime+.5);o.start();o.stop(actx.currentTime+.55)}catch(e){}}
function startTimer(min,label){
  try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();actx.resume()}catch(e){}
  let end=Date.now()+min*60000,ring=null;
  const el=document.createElement("div");el.className="timer";
  el.innerHTML=`<div><div class="lbl">${esc(label)}</div><div class="t"></div></div><button>+1 min</button><button aria-label="Close">✕</button>`;
  timersEl.appendChild(el);const [plus,close]=el.querySelectorAll("button");
  plus.onclick=()=>{end=Math.max(end,Date.now())+60000;el.classList.remove("ring");clearInterval(ring);ring=null};
  close.onclick=()=>{clearInterval(iv);clearInterval(ring);el.remove()};
  const tick=()=>{const s=Math.max(0,Math.round((end-Date.now())/1000));
    el.querySelector(".t").textContent=s?`${Math.floor(s/60)}:${String(s%60).padStart(2,"0")}`:"Done!";
    if(s===0&&!ring){el.classList.add("ring");beep();ring=setInterval(beep,1500)}};
  tick();const iv=setInterval(tick,500);
}
})();

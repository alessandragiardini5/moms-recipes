"""Run from the repo root:  python3 tools/build.py
Builds Mom's Recipe Box as a plain static website: index.html plus one page per
recipe in recipes/, each with schema.org Recipe JSON-LD (for Apple HomeView).
Recipe text lives in tools/recipes.py — edit that, never the generated HTML."""
import json, os, re, shutil, html, sys, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from recipes import RECIPES  # noqa: E402

E = html.escape

# Favorites database (Supabase). The publishable key is meant to be public.
SUPABASE_URL = "https://ppkuiafkfvsyzdcnurhs.supabase.co/rest/v1/favorites"
SUPABASE_KEY = "sb_publishable_Kuo6iWrCxMpjY94yLM19uQ_rAkgJCcH"

# ---------- amounts ----------
FRACS = [(0, ""), (1/8, "⅛"), (1/4, "¼"), (1/3, "⅓"), (3/8, "⅜"), (1/2, "½"),
         (5/8, "⅝"), (2/3, "⅔"), (3/4, "¾"), (7/8, "⅞"), (1, "")]
PLURAL = {"cup": "cups", "can": "cans", "cube": "cubes", "package": "packages",
          "loaf": "loaves", "handful": "handfuls", "bunch": "bunches", "strip": "strips",
          "square": "squares", "bag": "bags", "small bottle": "small bottles"}

def frac(x):
    w = int(x); r = x - w
    v, sym = min(FRACS, key=lambda f: abs(f[0] - r))
    if v == 1: w += 1
    return (str(w) if w else "") + sym or "0"

def us_amount(it):
    if "q" not in it: return ""
    q = it["q"]; top = it.get("q2", q); u = it.get("u", "")
    if u: u = PLURAL.get(u, u) if top > 1 else u
    num = frac(q) + ("–" + frac(it["q2"]) if "q2" in it else "")
    return (num + (" " + u if u else "")).strip()

def ing_text(it):
    t = " ".join(x for x in [it.get("pre", ""), us_amount(it), it["i"]] if x)
    notes = [n for n in [it.get("nus"), it.get("n")] if n]
    return t + (f" ({'; '.join(notes)})" if notes else "")

def temps(escaped):
    return re.sub(r"(\d{3})°F", r'<span class="temp" data-f="\1">\1°F</span>', escaped)

# ---------- page shell ----------
HEART = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.3s-7.4-4.5-9.5-9C1 8 2.7 4.6 6.1 4.2c2.2-.3 4.2.9 5.9 2.9 1.7-2 3.7-3.2 5.9-2.9 3.4.4 5.1 3.8 3.6 7.1-2.1 4.5-9.5 9-9.5 9z"/></svg>'

def fav_btn(rid, extra=""):
    return f'<button class="fav{extra}" data-id="{rid}" aria-pressed="false" aria-label="Add to favorites">{HEART}</button>'

def page(title, body, root, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Mom's Recipes">
<link rel="apple-touch-icon" href="{root}icon.png">
<title>{E(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Caveat:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css?v={VER["css"]}">
{extra_head}</head>
<body>
<header><div class="wrap">
  <a class="brand" href="{root}index.html"><span>Mom's</span><b>Recipe Box</b></a>
  <div class="tools"><button class="pill" id="bigBtn" aria-pressed="false">Large text</button></div>
</div></header>
<main class="wrap">
{body}
</main>
<div id="timers"></div>
<div id="lb"><img alt=""></div>
<div id="toast" role="status"></div>
<script>window.FAV={{url:"{SUPABASE_URL}",key:"{SUPABASE_KEY}"}};</script>
<script src="{root}app.js?v={VER["js"]}"></script>
</body>
</html>
"""

def jsonld(r):
    d = {"@context": "https://schema.org", "@type": "Recipe", "name": r["title"],
         "author": {"@type": "Person", "name": "Mom"},
         "image": [f"../cards/{r['card']}"],
         "recipeCategory": r["cat"],
         "recipeIngredient": [ing_text(i) for g in r["groups"] for i in g["items"]],
         "recipeInstructions": [{"@type": "HowToStep", "text": s["s"]} for s in r["steps"] if not s["s"].startswith("(")]}
    if r["cook"]: d["cookTime"] = d["totalTime"] = f"PT{r['cook']}M"
    return '<script type="application/ld+json">\n' + json.dumps(d, ensure_ascii=False, indent=1) + '\n</script>\n'

def ing_li(it, k):
    amt = ""
    if "q" in it:
        attrs = f'data-q="{it["q"]}"' + "".join(f' data-{a}="{E(str(it[a]))}"' for a in ("q2", "u", "gpc", "ge") if a in it)
        amt = (E(it["pre"]) + " " if it.get("pre") else "") + f'<span class="q" {attrs}>{E(us_amount(it))}</span> '
    note = (f' <span class="n nus">({E(it["nus"])})</span>' if it.get("nus") else "") + \
           (f' <span class="n">({E(it["n"])})</span>' if it.get("n") else "")
    return f'<li><label><input type="checkbox" data-k="{k}"><span>{amt}{E(it["i"])}{note}</span></label></li>'

def fact_html(f):
    if len(f) == 3:
        return f'<div class="fact"><b>{E(f[0])}</b><span class="fq" data-q="{f[2]}" data-w="{E(f[1])}">{(frac(f[2]) + " " + E(f[1])).strip()}</span></div>'
    return f'<div class="fact"><b>{E(f[0])}</b>{temps(E(f[1]))}</div>'

def recipe_page(r):
    k = 0; groups = []
    for g in r["groups"]:
        lis = []
        for it in g["items"]:
            lis.append(ing_li(it, k)); k += 1
        groups.append((f'<h3 class="sub">{E(g["name"])}</h3>' if g.get("name") else "") + '<ul class="ing">' + "".join(lis) + '</ul>')
    steps = "".join(
        f'<li data-i="{n}"><span class="stxt">{temps(E(s["s"]))}</span>'
        + (f' <button class="tbtn" data-t="{s["t"]}" data-l="{E(r["title"])}">⏱ {s["t"]} min</button>' if s.get("t") else "")
        + (' <span class="added">not on card</span>' if s.get("added") else "") + '</li>'
        for n, s in enumerate(r["steps"]))
    cook = json.dumps({"title": r["title"], "steps": [{"h": temps(E(s["s"])), "t": s.get("t")} for s in r["steps"]]}, ensure_ascii=False)
    notes = ('<div class="notes"><h2>To check with Mom</h2><ul>' + "".join(f"<li>{E(x)}</li>" for x in r["notes"]) + '</ul></div>') if r["notes"] else ""
    tips = ('<div class="notes tips"><h2>Mom&rsquo;s tips</h2><ul>' + "".join(f"<li>{E(x)}</li>" for x in r["tips"]) + '</ul></div>') if r.get("tips") else ""
    who = r.get("from", "Mom")
    back_img = f'<img class="cardimg cardback" src="../cards/{r["back"]}" alt="Back of the card">' if r.get("back") else ""
    body = f"""<a class="back" href="../index.html">← All recipes</a>
<article data-recipe="{r['id']}">
<section class="rhead">
  <div>
    <div class="kicker">{E(r['cat'])}</div>
    <div class="titlerow"><h1>{E(r['title'])}</h1>{fav_btn(r['id'], ' big')}</div>
    <div class="from">From the kitchen of {E(who)}</div>
    <div class="facts">{''.join(fact_html(f) for f in r['facts'])}</div>
    <div class="controls">
      <div class="seg" id="scale" role="group" aria-label="Recipe amount">
        <button data-m="0.5">½×</button><button data-m="1" aria-pressed="true">1×</button><button data-m="2">2×</button><button data-m="3">3×</button>
      </div>
      <div class="seg" id="units" role="group" aria-label="Units">
        <button data-units="us" aria-pressed="true">US</button><button data-units="metric">Metric</button>
      </div>
      <button class="cookbtn" id="cookBtn">Cook mode</button>
    </div>
  </div>
  <div><img class="cardimg" src="../cards/{r['card']}" alt="Original recipe card for {E(r['title'])}">
    {back_img}<div class="cardcap">{E(who)}'s original card{" (front and back)" if r.get("back") else ""} · tap to enlarge</div></div>
</section>
<section class="body">
  <div id="ingcol">
    <h2>Ingredients <small><button class="pill" id="clr">Reset</button></small></h2>
    {''.join(groups)}
  </div>
  <div>
    <h2>Method <small>tap a step to mark it done</small></h2>
    <ol class="steps">{steps}</ol>
    {tips}{notes}
  </div>
</section>
</article>
<div id="cook" hidden></div>
<script id="cookdata" type="application/json">{cook}</script>"""
    return page(f"{r['title']} · Mom's Recipe Box", body, "../", jsonld(r))

def flag(r):
    if r.get("incomplete"): return '<span class="flag">Front of card missing</span>'
    n = len(r["notes"])
    return f'<span class="flag">{n} thing{"s" if n > 1 else ""} to check</span>' if n else ""

def tile(r):
    words = " ".join([r["title"], r.get("from", "Mom")] + [i["i"] for g in r["groups"] for i in g["items"]]).lower()
    return (f'<a class="tile" href="recipes/{r["id"]}.html" data-id="{r["id"]}" data-cat="{E(r["cat"])}" data-words="{E(words)}">'
            f'{fav_btn(r["id"])}'
            f'<div class="ph" style="background-image:url(\'cards/{r["card"]}\')"></div>'
            f'<div class="bd"><div class="cat">{E(r["cat"])}</div><h3>{E(r["title"])}</h3>'
            f'<div class="meta">From the kitchen of {E(r.get("from", "Mom"))}</div>{flag(r)}</div></a>')

def index_page():
    cats = ["All"] + sorted({r["cat"] for r in RECIPES})
    body = f"""<section class="hero">
  <h1>From the kitchen of Mom</h1>
  <p>Recipes copied from her cow-print cards. {len(RECIPES)} recipes so far.</p>
</section>
<section class="favsec">
  <h2 class="sech"><span class="hearticon">{HEART}</span> Favorites</h2>
  <div class="grid" id="favgrid"></div>
  <div class="empty" id="favempty"><span class="hearticon outline">{HEART}</span><span>Tap the heart on any recipe to save it here.</span></div>
</section>
<h2 class="sech">All recipes</h2>
<div class="filters">
  <input class="search" id="q" placeholder="Search recipes or ingredients…" type="search">
  {''.join(f'<button class="pill" data-filter="{E(c)}" aria-pressed="{str(c == "All").lower()}">{E(c)}</button>' for c in cats)}
</div>
<div class="grid" id="grid">{''.join(tile(r) for r in RECIPES)}</div>
<p class="n" id="none" hidden>No recipes match.</p>"""
    return page("Mom's Recipe Box", body, "")

EXTRA_CSS = """
.kicker{color:var(--red);font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;font-weight:600}
.tile[hidden]{display:none}
/* favorites */
.tile{position:relative}
.fav{border:0;background:none;padding:0;cursor:pointer;display:grid;place-items:center;-webkit-tap-highlight-color:transparent}
.fav svg{width:22px;height:22px;fill:none;stroke:var(--red);stroke-width:2;transition:transform .15s}
.fav[aria-pressed="true"] svg{fill:var(--red)}
.fav:active svg{transform:scale(.85)}
.tile .fav{position:absolute;top:10px;right:10px;z-index:2;width:42px;height:42px;border-radius:50%;background:rgba(255,253,248,.95);box-shadow:0 1px 5px rgba(0,0,0,.18)}
.titlerow{display:flex;align-items:center;gap:14px}
.fav.big{width:48px;height:48px;border-radius:50%;border:1px solid var(--line);background:var(--card);flex:none}
.fav.big svg{width:26px;height:26px}
h2.sech{font-family:var(--serif);font-size:1.5rem;margin:28px 0 4px;display:flex;align-items:center;gap:8px;justify-content:flex-start}
.hearticon svg{width:22px;height:22px;fill:var(--red);stroke:none;display:block}
.favsec .grid{padding:14px 0 6px}
.empty{display:flex;align-items:center;gap:12px;color:var(--muted);font-size:.95rem;margin:12px 0 8px;padding:18px 20px;border:1.5px dashed var(--line);border-radius:14px;background:rgba(255,253,248,.6)}
.hearticon.outline svg{fill:none;stroke:var(--red);stroke-width:2}
.empty[hidden],#favgrid:empty{display:none}
/* scale / units / cook controls */
.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;align-items:center}
.seg{display:inline-flex;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:3px}
.seg button{border:0;background:none;border-radius:999px;padding:6px 13px;font-size:.88rem;color:var(--muted)}
.seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
.cookbtn{border:0;background:var(--red);color:#fff;border-radius:999px;padding:9px 18px;font-weight:600;font-size:.92rem}
body.metric .nus{display:none}
.q.scaled{color:var(--red)}
/* cook mode */
#cook{position:fixed;inset:0;z-index:35;background:var(--paper);display:flex;flex-direction:column}
#cook[hidden]{display:none}
.ck-top{display:flex;align-items:center;justify-content:space-between;padding:18px 28px;border-bottom:1px solid var(--line);background:var(--card);gap:12px}
.ck-title{font-family:var(--serif);font-weight:600;font-size:1.25rem}
.ck-count{color:var(--muted);font-size:.95rem;white-space:nowrap}
.ck-close{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:8px 16px}
.ck-main{flex:1;overflow:auto;padding:5vh 8vw;display:flex;flex-direction:column;justify-content:center}
.ck-step{font-family:var(--serif);font-size:clamp(1.7rem,3.6vw,2.9rem);line-height:1.3;max-width:28ch}
.ck-main h3{font-family:var(--serif);font-size:1.8rem;margin:0 0 12px}
.ck-main h4{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--red);margin:18px 0 4px}
.ck-main ul{list-style:none;padding:0;margin:0;font-size:clamp(1.15rem,2vw,1.5rem);columns:2 18ch;column-gap:48px}
.ck-main li{padding:6px 0;border-bottom:1px dashed var(--line);break-inside:avoid}
.ck-main .tbtn{font-size:1.1rem;padding:8px 18px;margin:22px 0 0}
.ck-bot{display:flex;justify-content:space-between;padding:16px 28px 22px;gap:12px}
.ck-bot button{flex:1;max-width:260px;border-radius:16px;padding:16px;font-size:1.1rem;font-weight:600;border:1px solid var(--line);background:var(--card)}
.ck-bot .next{background:var(--ink);color:#fff;border-color:var(--ink);margin-left:auto}
.ck-dots{display:flex;gap:6px;justify-content:center;padding-bottom:4px}
.ck-dots i{width:8px;height:8px;border-radius:50%;background:var(--line)}
.ck-dots i.on{background:var(--red)}
#timers{z-index:40}
#toast{position:fixed;left:50%;top:20px;transform:translateX(-50%);background:var(--ink);color:#fff;padding:10px 18px;border-radius:12px;font-size:.9rem;z-index:50;opacity:0;pointer-events:none;transition:opacity .2s}
#toast.on{opacity:1}
@media (max-width:820px){.ck-main{padding:4vh 22px}.ck-top,.ck-bot{padding-left:18px;padding-right:18px}}
"""

APP_JS = r"""/* Mom's Recipe Box — shared script for every page */
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
    if(!r.ok)throw 0;
  }catch(e){on?favs.delete(id):favs.add(id);store.set("favs",[...favs]);paintFavs();toast("Couldn't save the favorite. Check the internet connection and try again.")}
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
const PL={cup:"cups",can:"cans",cube:"cubes",package:"packages",loaf:"loaves",handful:"handfuls",bunch:"bunches",strip:"strips",square:"squares",bag:"bags","small bottle":"small bottles"};
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
    else h+="<ul>"+$$("li",el).map(li=>`<li>${$("label > span",li).innerHTML}</li>`).join("")+"</ul>"});return h}
  function show(){
    const s=idx===0?null:data.steps[idx-1];
    ck.innerHTML=`<div class="ck-top"><div><div class="ck-title">${esc(data.title)}</div><div class="ck-count">${idx===0?"Ingredients":"Step "+idx+" of "+data.steps.length}</div></div>
      <button class="ck-close">Close</button></div>
      <div class="ck-main">${idx===0?`<h3>Ingredients</h3>${ingHTML()}`:`<div class="ck-step">${s.h}</div>${s.t?`<div><button class="tbtn" data-t="${s.t}">⏱ Start ${s.t}-min timer</button></div>`:""}`}</div>
      <div class="ck-dots">${Array.from({length:slides},(_,i)=>`<i class="${i===idx?"on":""}"></i>`).join("")}</div>
      <div class="ck-bot">${idx>0?'<button class="prev">← Back</button>':""}<button class="next">${idx===slides-1?"Done":idx===0?"Start cooking →":"Next →"}</button></div>`;
    renderAmounts(ck);
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
"""

README = """# Mom's Recipe Box

Live at https://alessandragiardini5.github.io/moms-recipes/ — a plain static site on GitHub Pages.

- tools/recipes.py      — ALL recipe text (the only file to edit for recipes)
- tools/build.py        — generates the pages: run `python3 tools/build.py`
- index.html            — recipe list, Favorites section, search and categories (generated)
- recipes/<name>.html   — one page per recipe with schema.org Recipe markup (generated)
- cards/                — photos of Mom's original cards; cards/on-hold/ for unfinished ones
- style.css, app.js     — look and behavior: checklists, timers, scaling, metric, cook mode, favorites (generated)
- Favorites are shared through a free Supabase table (the free plan pauses after about a week without activity).
"""

VER = {}

if __name__ == "__main__":
    shutil.rmtree(os.path.join(ROOT, "recipes"), ignore_errors=True)
    os.makedirs(os.path.join(ROOT, "recipes"))
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    css = open(os.path.join(ROOT, "tools/base.css")).read() + EXTRA_CSS
    VER["css"] = hashlib.sha1(css.encode()).hexdigest()[:8]
    VER["js"] = hashlib.sha1(APP_JS.encode()).hexdigest()[:8]
    open(os.path.join(ROOT, "style.css"), "w").write(css)
    open(os.path.join(ROOT, "app.js"), "w").write(APP_JS)
    open(os.path.join(ROOT, "README.md"), "w").write(README)
    open(os.path.join(ROOT, "index.html"), "w").write(index_page())
    for r in RECIPES:
        open(os.path.join(ROOT, "recipes", r["id"] + ".html"), "w").write(recipe_page(r))
    print("built", len(RECIPES), "recipes")

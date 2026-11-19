"""Run: python3 tools/build.py
Builds Mom's Recipe Box as a plain static website (one HTML page per recipe,
schema.org Recipe JSON-LD on each). Output: /home/claude/mums-recipes/"""
import json, os, shutil, html

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
E = html.escape

RECIPES = [
{
 "id":"hello-dollies","title":"Hello Dollies","cat":"Desserts","date":"March 2001 (card says “3-01”)",
 "card":"hello-dollies.jpg","facts":[["Oven","350°F"],["Bake","25 min"]],"cook":25,
 "groups":[{"items":[
   ["1 cube","butter, melted","(1 stick / ½ cup)"],["1½ cups","graham cracker crumbs"],
   ["1 cup","chopped walnuts"],["1 cup","chocolate chips"],["1⅓ cups","flaked coconut"],
   ["1 can","Eagle Brand sweetened condensed milk"],["12 oz","butterscotch chips"]]}],
 "steps":[
   {"s":"Layer everything in a baking pan: melted butter, then the graham crumbs, walnuts, chocolate chips, butterscotch chips and coconut; pour the condensed milk evenly over the top."},
   {"s":"Bake at 350°F for 25 minutes.","t":25},
   {"s":"Cool before cutting into bars."}],
 "notes":[]
},
{
 "id":"cheesecake","title":"Cheesecake","cat":"Desserts","date":"Dec 28, 1993",
 "card":"cheesecake.jpg","facts":[["Oven","350°F, then 450°F"],["Bake","20–25 + 5 min"],["Makes","2 cheesecakes"]],"cook":30,
 "groups":[
   {"name":"Crust","items":[["","graham cracker crumbs","— use the crust recipe on the box"]]},
   {"name":"Filling","items":[["3 × 8 oz","packages cream cheese"],["1 cup","sugar"],["4","eggs"]]},
   {"name":"Topping","items":[["½ cup","sugar"],["1 tsp","vanilla"],["2 cups","sour cream","(16 oz)"]]}],
 "steps":[
   {"s":"Make the graham cracker crust following the recipe on the crumb box."},
   {"s":"Beat the cream cheese, sugar and eggs together."},
   {"s":"Pour into the crust and bake at 350°F for 20–25 minutes (start checking at 20).","t":25},
   {"s":"Cool 20 minutes before adding the topping.","t":20},
   {"s":"Mix the sugar, vanilla and sour cream; spread over the top."},
   {"s":"Bake at 450°F for 5 minutes.","t":5}],
 "notes":[]
},
{
 "id":"cheese-bread","title":"Cheese Bread","cat":"Breads & Sides","date":"Dec 28, 1993",
 "card":"cheese-bread.jpg","facts":[["Oven","400°F"],["Bake","10 min"]],"cook":10,
 "groups":[{"items":[["1 loaf","day-old sliced bread"],["3","eggs"],["3 tsp","milk"],["","melted butter"],["","Parmesan cheese"]]}],
 "steps":[
   {"s":"Remove the crusts from the bread."},
   {"s":"Beat the eggs and milk into a batter."},
   {"s":"Work in stacks of 3 slices: leave the 1st slice plain, dip the 2nd slice in the egg-and-milk batter, leave the 3rd slice plain."},
   {"s":"Stack all three together, with the battered slice in the middle."},
   {"s":"Coat the bread in melted butter and Parmesan cheese."},
   {"s":"Bake at 400°F for 10 minutes.","t":10}],
 "notes":[]
},
{
 "id":"crab-dip","title":"Crab Dip","cat":"Appetizers","date":"Dec 28, 1993",
 "card":"crab-dip.jpg","facts":[["Cook","No cooking"],["Serve","Chilled"]],"cook":0,
 "groups":[{"items":[["1 cup","cream cheese"],["1 tbsp","lemon juice"],["½ tsp","salt"],["¼ tsp","paprika"],
                     ["1 can","crab"],["½ tsp","ground mustard"],["","red food coloring","(if desired)"]]}],
 "steps":[{"s":"Mix everything together and refrigerate."},{"s":"Serve with water crackers!"}],
 "notes":[]
}
]

# On hold until the front of the card is photographed
ON_HOLD = [
{
 "id":"apple-pie","title":"Apple Pie","cat":"Desserts","date":"Undated","incomplete":True,
 "card":"apple-pie-back.jpg","facts":[["Oven","425°F"],["Bake","50–60 min"]],"cook":60,
 "groups":[{"name":"From the back of the card","items":[["","apples"],["","pie crust","(bottom and top)"],
            ["1 handful","water"],["½","lemon, juiced"],["1½ tsp","butter, dotted"]]}],
 "steps":[
   {"s":"(The beginning of the recipe is on the front of the card — not photographed yet.)","added":True},
   {"s":"…apples in a bowl, or pour over in the pie shell."},
   {"s":"Drip a handful of water over the apples."},
   {"s":"Squeeze the juice of ½ lemon over the apples before adding 1½ tsp dotted butter."},
   {"s":"Place the top crust over the pie and crimp."},
   {"s":"Bake at 425°F for 50–60 minutes.","t":60}],
 "notes":["Only the back of this card was in the batch — please photograph the front (ingredients and the first steps).",
          "Different handwriting and card from the others — whose recipe is it?",
          "The 50–60 min timer is set to 60; start checking at 50."]
}
]

LOGO = '<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><rect x="2" y="6" width="30" height="22" rx="3" fill="#fff" stroke="#c8323c" stroke-width="2.5"/><ellipse cx="9" cy="13" rx="3.2" ry="2.4" fill="#2b2420"/><ellipse cx="24" cy="21" rx="4" ry="2.8" fill="#2b2420"/><ellipse cx="22" cy="11" rx="1.8" ry="1.4" fill="#2b2420"/></svg>'

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
<link rel="stylesheet" href="{root}style.css">
{extra_head}</head>
<body>
<header><div class="wrap">
  <a class="brand" href="{root}index.html">{LOGO}<b>Mom's Recipe Box</b></a>
  <div class="tools"><button class="pill" id="bigBtn" aria-pressed="false">Large text</button></div>
</div></header>
<main class="wrap">
{body}
</main>
<div id="timers"></div>
<div id="lb"><img alt=""></div>
<script src="{root}app.js"></script>
</body>
</html>
"""

def iso(m): return f"PT{m}M" if m else None

def jsonld(r):
    d = {"@context":"https://schema.org","@type":"Recipe","name":r["title"],
         "author":{"@type":"Person","name":"Mom"},
         "image":[f"../cards/{r['card']}"],
         "recipeCategory":r["cat"],
         "recipeIngredient":[" ".join(x for x in i if x).strip() for g in r["groups"] for i in g["items"]],
         "recipeInstructions":[{"@type":"HowToStep","text":s["s"]} for s in r["steps"] if not s["s"].startswith("(")]}
    if r["cook"]: d["cookTime"]=iso(r["cook"]); d["totalTime"]=iso(r["cook"])
    return '<script type="application/ld+json">\n'+json.dumps(d,ensure_ascii=False,indent=1)+'\n</script>\n'

def recipe_page(r):
    groups=[]
    k=0
    for g in r["groups"]:
        lis=[]
        for i in g["items"]:
            q,item,note=(i+[""])[:3]
            lis.append(f'<li><label><input type="checkbox" data-k="{k}"><span>'
                       +(f'<span class="q">{E(q)}</span> ' if q else "")+E(item)
                       +(f' <span class="n">{E(note)}</span>' if note else "")+'</span></label></li>')
            k+=1
        groups.append((f'<h3 class="sub">{E(g["name"])}</h3>' if g.get("name") else "")+'<ul class="ing">'+"".join(lis)+'</ul>')
    steps="".join(
        f'<li data-i="{n}">{E(s["s"])}'
        +(f' <button class="tbtn" data-t="{s["t"]}" data-l="{E(r["title"])}">⏱ {s["t"]} min</button>' if s.get("t") else "")
        +(' <span class="added">not on card</span>' if s.get("added") else "")+'</li>'
        for n,s in enumerate(r["steps"]))
    notes=('<div class="notes"><h2>To check with Mom</h2><ul>'+"".join(f"<li>{E(x)}</li>" for x in r["notes"])+'</ul></div>') if r["notes"] else ""
    facts="".join(f'<div class="fact"><b>{E(a)}</b>{E(b)}</div>' for a,b in r["facts"])
    body=f"""<a class="back" href="../index.html">← All recipes</a>
<article data-recipe="{r['id']}">
<section class="rhead">
  <div>
    <div class="kicker">{E(r['cat'])}</div>
    <h1>{E(r['title'])}</h1>
    <div class="from">From the kitchen of Mom · {E(r['date'])}</div>
    <div class="facts">{facts}</div>
  </div>
  <div><img class="cardimg" src="../cards/{r['card']}" alt="Mom's original recipe card for {E(r['title'])}">
    <div class="cardcap">Mom's original card · tap to enlarge</div></div>
</section>
<section class="body">
  <div>
    <h2>Ingredients <small><button class="pill" id="clr">Reset</button></small></h2>
    {''.join(groups)}
  </div>
  <div>
    <h2>Method <small>tap a step to mark it done</small></h2>
    <ol class="steps">{steps}</ol>
    {notes}
  </div>
</section>
</article>"""
    return page(f"{r['title']} · Mom's Recipe Box", body, "../", jsonld(r))

def index_page():
    cats=["All"]+sorted({r["cat"] for r in RECIPES})
    tiles=[]
    for r in RECIPES:
        words=" ".join([r["title"]]+[i[1] for g in r["groups"] for i in g["items"]]).lower()
        flag='<span class="flag">Front of card missing</span>' if r.get("incomplete") else (
            f'<span class="flag">{len(r["notes"])} thing{"s" if len(r["notes"])>1 else ""} to check</span>' if r["notes"] else "")
        tiles.append(f'<a class="tile" href="recipes/{r["id"]}.html" data-cat="{E(r["cat"])}" data-words="{E(words)}">'
                     f'<div class="ph" style="background-image:url(\'cards/{r["card"]}\')"></div>'
                     f'<div class="bd"><div class="cat">{E(r["cat"])}</div><h3>{E(r["title"])}</h3>'
                     f'<div class="meta">{E(r["date"])}</div>{flag}</div></a>')
    body=f"""<section class="hero">
  <h1>From the kitchen of Mom</h1>
  <p>Recipes copied from her cow-print cards. {len(RECIPES)} recipes so far.</p>
</section>
<div class="filters">
  <input class="search" id="q" placeholder="Search recipes or ingredients…" type="search">
  {''.join(f'<button class="pill" data-filter="{E(c)}" aria-pressed="{str(c=="All").lower()}">{E(c)}</button>' for c in cats)}
</div>
<div class="grid" id="grid">{''.join(tiles)}</div>
<p class="n" id="none" hidden>No recipes match.</p>"""
    return page("Mom's Recipe Box", body, "")

EXTRA_CSS = """
.kicker{color:var(--red);font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;font-weight:600}
.tile[hidden]{display:none}
"""

APP_JS = r"""/* Mom's Recipe Box — shared script for every page */
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
"""

README = """# Mom's Recipe Box

A plain static website: no build step, no server. Open index.html in any browser,
or upload this whole folder to a free host (GitHub Pages or Netlify Drop) to get a
normal web address that opens in Safari.

- index.html            — recipe list with search and categories
- recipes/<name>.html   — one page per recipe (with schema.org Recipe markup for HomeView)
- cards/                — photos of Mom's original cards
- style.css, app.js     — shared look and behavior (checklists, timers, large text)
- tools/build.py        — the recipe text lives here; run it to regenerate the pages
- cards/on-hold/        — photos of cards not yet on the site
"""

shutil.rmtree(OUT+"/recipes", ignore_errors=True); os.makedirs(OUT+"/recipes")
open(OUT+"/.nojekyll","w").close()
open(OUT+"/style.css","w").write(open(OUT+"/tools/base.css").read()+EXTRA_CSS)
open(OUT+"/app.js","w").write(APP_JS)
open(OUT+"/README.md","w").write(README)
open(OUT+"/index.html","w").write(index_page())
for r in RECIPES: open(f"{OUT}/recipes/{r['id']}.html","w").write(recipe_page(r))

# home-screen icon
from PIL import Image, ImageDraw
im=Image.new("RGB",(180,180),"#faf6ee");d=ImageDraw.Draw(im)
d.rounded_rectangle((18,40,162,140),12,fill="white",outline="#c8323c",width=8)
for b in [(40,62,72,86),(104,100,144,126),(100,58,118,72)]: d.ellipse(b,fill="#2b2420")
im.save(OUT+"/icon.png")
print("built", len(RECIPES), "recipes")

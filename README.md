# Mom's Recipe Box

A plain static website: no build step, no server. Open index.html in any browser,
or upload this whole folder to a free host (GitHub Pages or Netlify Drop) to get a
normal web address that opens in Safari.

- index.html            — recipe list with search and categories
- recipes/<name>.html   — one page per recipe (with schema.org Recipe markup for HomeView)
- cards/                — photos of Mom's original cards
- style.css, app.js     — shared look and behavior (checklists, timers, large text)
- tools/build.py        — the recipe text lives here; run it to regenerate the pages
- cards/on-hold/        — photos of cards not yet on the site

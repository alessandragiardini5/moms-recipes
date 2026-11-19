# Mom's Recipe Box

Live at https://alessandragiardini5.github.io/moms-recipes/ — a plain static site on GitHub Pages.

- tools/recipes.py      — ALL recipe text (the only file to edit for recipes)
- tools/build.py        — generates the pages: run `python3 tools/build.py`
- index.html            — recipe list, Favorites section, search and categories (generated)
- recipes/<name>.html   — one page per recipe with schema.org Recipe markup (generated)
- cards/                — photos of Mom's original cards; cards/on-hold/ for unfinished ones
- style.css, app.js     — look and behavior: checklists, timers, scaling, metric, cook mode, favorites (generated)
- Favorites are shared through a free Supabase table (the free plan pauses after about a week without activity).

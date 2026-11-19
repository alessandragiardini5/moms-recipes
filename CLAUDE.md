# Mom's Recipe Box — instructions for Claude

Live site: https://alessandragiardini5.github.io/moms-recipes/ (GitHub Pages, branch main, root).

## How the site is built
- All recipe text lives in `tools/recipes.py` (`RECIPES`; `ON_HOLD` for recipes waiting on info). Its docstring explains every field. Amounts are numbers + units (`q`, `q2` for ranges, `u`, `pre` for "about") so the ½×–3× scaler and US/metric toggle work; add `gpc` (grams per cup) for dry/solid cup ingredients and `ge` (grams each) for cans/cubes/packages/squares/bags. Never put amounts in the ingredient text.
- Run `python3 tools/build.py` from the repo root to regenerate `index.html` and `recipes/*.html`. Never hand-edit generated HTML.
- Shared look: `tools/base.css` + EXTRA_CSS in build.py → `style.css`. Behavior: `app.js` (written by build.py): checklists, timers, scaling, metric, cook mode, favorites.
- Favorites are shared by all visitors via a Supabase table `favorites(recipe_id)` (URL + publishable key in build.py; the key is public by design). The free project pauses after ~1 week of low activity (data kept; resume from the Supabase dashboard). A daily keep-alive GitHub Actions workflow was proposed but not added — Ali hasn't approved it. The Claude sandbox can't reach supabase.co; test favorites in headless Chrome with request interception.
- Only one chat should push to this repo at a time. Always `git fetch` and rebase on origin/main before pushing; never force-push.
- Card photos: `cards/<recipe-id>.jpg` — rotate upright, max 1400px, JPEG quality ~72. Check orientation visually (EXIF can be wrong). Held cards go in `cards/on-hold/`.
- Each recipe page carries schema.org Recipe JSON-LD (for Apple HomeView). Put times in steps as `"t": minutes` so they get timer buttons and cookTime.

## Conventions
- Always "Mom", never "Mum". American English spelling.
- Not every card is Mom's: cards signed "A. Dotson" (Angela Dotson) get `"from":"Angela"` → "From the kitchen of Angela". Default is Mom.
- No dates shown on thumbnails or recipe pages — just "From the kitchen of Mom".
- Card tips from Mom go in `"tips"` (shown as "Mom's tips"); `"notes"` is only for open questions (shows "To check with Mom" + a flag on the tile).
- If Mom gives no amount (e.g. butter, Parmesan), leave it without a quantity.
- Steps not on the card get `"added": True` (shows "not on card") unless Ali approves them.

## Workflow per batch
1. Ali sends card photos.
2. Transcribe; send a numbered review checklist (transcription + questions) in chat.
3. Ali answers (with Mom); apply answers; put unresolved recipes in ON_HOLD.
4. Rebuild, screenshot-check, commit, push → site updates in ~1 min.
5. Update the project doc `claude/recipe-transcriptions.md` with the batch log.

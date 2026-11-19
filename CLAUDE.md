# Mom's Recipe Box — instructions for Claude

Live site: https://alessandragiardini5.github.io/moms-recipes/ (GitHub Pages, branch main, root).

## How the site is built
- All recipe text lives in `tools/build.py` (the `RECIPES` list; `ON_HOLD` for recipes waiting on info).
- Run `python3 tools/build.py` from the repo root to regenerate `index.html` and `recipes/*.html`. Never hand-edit generated HTML.
- Shared look: `tools/base.css` (source) → `style.css` (generated). Behavior: `app.js` (written by build.py).
- Card photos: `cards/<recipe-id>.jpg` — rotate upright, max 1400px, JPEG quality ~72. Check orientation visually (EXIF can be wrong). Held cards go in `cards/on-hold/`.
- Each recipe page carries schema.org Recipe JSON-LD (for Apple HomeView). Put times in steps as `"t": minutes` so they get timer buttons and cookTime.

## Conventions
- Always "Mom", never "Mum". American English spelling.
- No dates shown on thumbnails or recipe pages — just "From the kitchen of Mom".
- If Mom gives no amount (e.g. butter, Parmesan), leave it without a quantity.
- Steps not on the card get `"added": True` (shows "not on card") unless Ali approves them.

## Workflow per batch
1. Ali sends card photos.
2. Transcribe; send a numbered review checklist (transcription + questions) in chat.
3. Ali answers (with Mom); apply answers; put unresolved recipes in ON_HOLD.
4. Rebuild, screenshot-check, commit, push → site updates in ~1 min.
5. Update the project doc `claude/recipe-transcriptions.md` with the batch log.

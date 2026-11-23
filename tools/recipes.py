"""Mom's recipes — the only file to edit when adding or correcting recipes.

Recipe fields: id, title, sub (English subtitle for Italian titles), cat, card (photo in cards/), back (optional photo of the card's back),
from (default "Mom"; "Angela" for cards signed A. Dotson), fromline (replaces the whole
"From the kitchen of …" line, e.g. "From Neiman Marcus"), cook (minutes, for HomeView),
facts, groups, steps, tips (Mom's tips shown as "Mom's tips"), notes (open questions only).

Ingredient fields:
  q    amount as a number (1.5, 4/3, 0.25) — leave out when the card gives none
  q2   upper end of a range ("¾–1 cup" -> q 0.75, q2 1)
  pre  word before the amount, e.g. "about"
  u    unit, singular: cup, tbsp, tsp, oz, lb, can, cube, package, loaf, handful, bunch, strip,
       square, bag, small bottle, glass, pinch, slice (none for "3 eggs")
  i    the ingredient
  n    note shown in every mode, e.g. "if desired"
  nus  note shown only in US units, e.g. "8 oz each"
  gpc  grams per cup — metric shows grams instead of ml for this cup ingredient
  ge   grams per unit — for cans/cubes/packages/squares, metric shows grams
Metric mode: cups -> grams (gpc) or ml; oz/lb -> grams; tsp/tbsp stay as spoons; °F -> °C.

Steps: "s" text (write temps as 350°F), "t" timer minutes, "added": True if not on the card.
Facts: [label, text] or [label, text, number] — the number scales with the recipe.
"""

RECIPES = [
{
 "id":"hello-dollies","title":"Hello Dollies","cat":"Desserts",
 "card":"hello-dollies.jpg","cook":25,
 "facts":[["Oven","350°F"],["Bake","25 min"]],
 "groups":[{"items":[
   {"q":1,"u":"cube","i":"butter, melted","n":"1 cube = 1 stick","ge":113},
   {"q":1.5,"u":"cup","i":"graham cracker crumbs","gpc":100},
   {"q":1,"u":"cup","i":"chopped walnuts","gpc":120},
   {"q":1,"u":"cup","i":"chocolate chips","gpc":170},
   {"q":4/3,"u":"cup","i":"flaked coconut","gpc":85},
   {"q":1,"u":"can","i":"Eagle Brand sweetened condensed milk","nus":"14 oz","ge":397},
   {"q":12,"u":"oz","i":"butterscotch chips"}]}],
 "steps":[
   {"s":"Layer everything in a baking pan: melted butter, then the graham crumbs, walnuts, chocolate chips, butterscotch chips and coconut; pour the condensed milk evenly over the top."},
   {"s":"Bake at 350°F for 25 minutes.","t":25},
   {"s":"Cool before cutting into bars."}],
 "notes":[]
},
{
 "id":"cheesecake","title":"Cheesecake","cat":"Desserts",
 "card":"cheesecake.jpg","cook":30,
 "facts":[["Oven","350°F, then 450°F"],["Bake","20–25 + 5 min"],["Makes","cheesecakes",2]],
 "groups":[
   {"name":"Crust","items":[{"i":"graham cracker crumbs","n":"use the crust recipe on the box"}]},
   {"name":"Filling","items":[
     {"q":3,"u":"package","i":"cream cheese","nus":"8 oz each","ge":227},
     {"q":1,"u":"cup","i":"sugar","gpc":200},
     {"q":4,"i":"eggs"}]},
   {"name":"Topping","items":[
     {"q":0.5,"u":"cup","i":"sugar","gpc":200},
     {"q":1,"u":"tsp","i":"vanilla"},
     {"q":2,"u":"cup","i":"sour cream","nus":"16 oz","gpc":240}]}],
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
 "id":"cheese-bread","title":"Cheese Bread","cat":"Breads & Sides",
 "card":"cheese-bread.jpg","cook":10,
 "facts":[["Oven","400°F"],["Bake","10 min"]],
 "groups":[{"items":[
   {"q":1,"u":"loaf","i":"day-old sliced bread"},
   {"q":3,"i":"eggs"},
   {"q":3,"u":"tsp","i":"milk"},
   {"i":"melted butter"},
   {"i":"Parmesan cheese"}]}],
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
 "id":"crab-dip","title":"Crab Dip","cat":"Appetizers",
 "card":"crab-dip.jpg","cook":0,
 "facts":[["Cook","No cooking"],["Serve","Chilled"]],
 "groups":[{"items":[
   {"q":1,"u":"cup","i":"cream cheese","gpc":225},
   {"q":1,"u":"tbsp","i":"lemon juice"},
   {"q":0.5,"u":"tsp","i":"salt"},
   {"q":0.25,"u":"tsp","i":"paprika"},
   {"q":1,"u":"can","i":"crab"},
   {"q":0.5,"u":"tsp","i":"ground mustard"},
   {"i":"red food coloring","n":"if desired"}]}],
 "steps":[{"s":"Mix everything together and refrigerate."},{"s":"Serve with water crackers!"}],
 "notes":[]
},
{
 "id":"apple-pie","title":"Apple Pie","cat":"Desserts",
 "card":"apple-pie.jpg","back":"apple-pie-back.jpg","cook":60,
 "facts":[["Oven","425°F"],["Bake","50–60 min"],["Size","9-inch pie"],["Serves","",8]],
 "groups":[
   {"name":"Filling","items":[
     {"q":0.75,"q2":1,"u":"cup","i":"sugar","gpc":200},
     {"q":0.5,"u":"tsp","i":"cinnamon"},
     {"q":0.5,"u":"tsp","i":"nutmeg"},
     {"pre":"about","q":7,"i":"pippin or Granny Smith apples","n":"peeled and sliced"},
     {"q":1,"u":"handful","i":"water"},
     {"q":0.5,"i":"lemon, juiced"},
     {"q":1.5,"u":"tsp","i":"butter","n":"dotted"}]},
   {"name":"Crust","items":[{"i":"pie crust","n":"bottom and top"}]}],
 "steps":[
   {"s":"Peel and slice about 7 pippin or Granny Smith apples."},
   {"s":"Mix the sugar and spices."},
   {"s":"Either stir the sugar mixture through the apples in a bowl, or pour it over the apples in the pie shell."},
   {"s":"Drip a handful of water over the apples."},
   {"s":"Squeeze the juice of ½ lemon over the apples, then dot with 1½ tsp butter."},
   {"s":"Place the top crust over the pie and crimp."},
   {"s":"Bake at 425°F for 50–60 minutes (start checking at 50).","t":60}],
 "notes":[]
},
{
 "id":"chocolate-chip-cookies","title":"Chocolate Chip Cookies","cat":"Desserts","from":"Angela",
 "card":"chocolate-chip-cookies.jpg","cook":11,
 "facts":[["Oven","375°F"],["Bake","9–11 min"],["Source","Nestlé Toll House package, taped to Mom's card"]],
 "groups":[{"items":[
   {"q":2.25,"u":"cup","i":"all-purpose flour","gpc":125},
   {"q":1,"u":"tsp","i":"baking soda"},
   {"q":1,"u":"tsp","i":"salt"},
   {"q":1,"u":"cup","i":"butter, softened","nus":"2 sticks","gpc":227},
   {"q":0.75,"u":"cup","i":"granulated sugar","gpc":200},
   {"q":0.75,"u":"cup","i":"packed brown sugar","gpc":220},
   {"q":1,"u":"tsp","i":"vanilla extract"},
   {"q":2,"i":"eggs"},
   {"q":2,"u":"cup","i":"semi-sweet chocolate morsels","nus":"12 oz package","gpc":170},
   {"q":1,"u":"cup","i":"chopped nuts","gpc":120}]}],
 "steps":[
   {"s":"Preheat the oven to 375°F."},
   {"s":"In a small bowl, combine the flour, baking soda and salt."},
   {"s":"In a large mixer bowl, beat the butter, both sugars and the vanilla until creamy."},
   {"s":"Add the eggs one at a time, beating well after each."},
   {"s":"Gradually beat in the flour mixture, then stir in the chocolate morsels and nuts."},
   {"s":"Drop by rounded tablespoons onto ungreased baking sheets."},
   {"s":"Bake 9–11 minutes, until golden brown (start checking at 9).","t":11},
   {"s":"Let stand on the sheets for 2 minutes, then move to wire racks to cool completely.","t":2}],
 "notes":[]
},
{
 "id":"spinach-salad","title":"Spinach Salad","cat":"Salads",
 "card":"spinach-salad.jpg","back":"spinach-salad-back.jpg","cook":0,
 "facts":[["Oven","None"],["Dressing","Shake in a jar"]],
 "groups":[
   {"name":"Salad","items":[
     {"q":1,"q2":2,"u":"bunch","i":"spinach","n":"washed and dried"},
     {"q":0.5,"u":"cup","i":"slivered almonds","n":"toasted","gpc":110},
     {"q":3,"u":"strip","i":"bacon","n":"crisp, crumbled"},
     {"q":1,"i":"red apple","n":"chopped, peel on"},
     {"i":"lemon juice"}]},
   {"name":"Dressing","items":[
     {"q":1/3,"u":"cup","i":"oil"},
     {"q":0.25,"u":"cup","i":"tarragon vinegar"},
     {"q":0.5,"u":"cup","i":"sugar","gpc":200},
     {"q":0.5,"u":"tsp","i":"dry mustard"},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"i":"pepper","n":"to taste, about ⅛ tsp"}]}],
 "steps":[
   {"s":"Combine the spinach, toasted almonds, crumbled bacon, chopped apple and lemon juice."},
   {"s":"Dressing: mix together the oil, tarragon vinegar, sugar, dry mustard, salt and pepper."},
   {"s":"Shake well, pour over the salad and toss."}],
 "notes":[]
},
{
 "id":"black-bottom-cupcakes","title":"Black Bottom Cupcakes","cat":"Desserts",
 "card":"black-bottom-cupcakes.jpg","back":"black-bottom-cupcakes-back.jpg","cook":30,
 "facts":[["Oven","350°F"],["Bake","25–30 min"],["Minis","15 min"]],
 "groups":[
   {"name":"Cream cheese topping","items":[
     {"q":1,"u":"cup","i":"cream cheese","nus":"8 oz package","gpc":227},
     {"q":1,"i":"egg"},
     {"q":1/3,"u":"cup","i":"sugar","gpc":200},
     {"q":0.125,"u":"tsp","i":"salt"},
     {"q":1,"u":"cup","i":"semi-sweet chocolate chips","nus":"6 oz package","gpc":170}]},
   {"name":"Chocolate batter — sift","items":[
     {"q":1.5,"u":"cup","i":"flour","gpc":125},
     {"q":1,"u":"cup","i":"sugar","gpc":200},
     {"q":1,"u":"tsp","i":"baking soda"},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"q":0.25,"u":"cup","i":"cocoa","gpc":85}]},
   {"name":"Chocolate batter — add and beat","items":[
     {"q":1,"u":"cup","i":"water"},
     {"q":1/3,"u":"cup","i":"oil"},
     {"q":1,"u":"tbsp","i":"white vinegar"},
     {"q":1,"u":"tsp","i":"vanilla"}]}],
 "steps":[
   {"s":"Topping: mix the cream cheese, egg, sugar and salt; stir in the chocolate chips."},
   {"s":"Sift together the flour, sugar, baking soda, salt and cocoa."},
   {"s":"Add the water, oil, vinegar and vanilla, and beat."},
   {"s":"Fill cupcake cups ½ full with the chocolate batter, then top each with a small scoop of the cream cheese topping."},
   {"s":"Bake at 350°F for 25–30 minutes (start checking at 25).","t":30},
   {"s":"For mini cupcakes, bake 15 minutes.","t":15}],
 "notes":[]
},
{
 "id":"punch","title":"Punch","cat":"Drinks",
 "card":"punch.jpg","cook":0,
 "facts":[["Cook","No cooking"],["Contains","Alcohol"]],
 "groups":[{"items":[
   {"q":1,"u":"small bottle","i":"cognac or brandy"},
   {"q":1,"u":"can","i":"crushed pineapple"},
   {"i":"Chablis (white wine)"}]}],
 "steps":[
   {"s":"Soak the crushed pineapple in the cognac or brandy."},
   {"s":"Add the Chablis."}],
 "notes":[]
},
{
 "id":"stuffed-baked-potatoes","title":"Stuffed Baked Potatoes","cat":"Breads & Sides",
 "card":"stuffed-baked-potatoes.jpg","back":"stuffed-baked-potatoes-back.jpg","cook":90,
 "facts":[["Oven","350°F"],["Bake","1 hr + 30 min"],["Makes","potatoes",8]],
 "groups":[{"items":[
   {"q":8,"i":"russet potatoes"},
   {"q":1,"u":"cup","i":"sour cream","gpc":240},
   {"q":2/3,"u":"cup","i":"milk"},
   {"q":0.25,"u":"cup","i":"Parmesan cheese","gpc":100},
   {"q":0.75,"u":"tsp","i":"salt"},
   {"q":0.25,"u":"tsp","i":"pepper"},
   {"q":2,"u":"tsp","i":"parsley flakes"},
   {"i":"Crisco","n":"for greasing the skins"},
   {"i":"grated cheddar cheese"},
   {"i":"paprika"}]}],
 "steps":[
   {"s":"Grease the potato skins with Crisco."},
   {"s":"Bake 1 hour at 350°F, or until soft when pricked with a fork.","t":60},
   {"s":"Let cool. Cut off the top of each potato and scoop out the inside."},
   {"s":"Mix the scooped-out potato with the sour cream, milk, Parmesan, parsley flakes, salt and pepper."},
   {"s":"Restuff the potatoes with the mixture and top with grated cheddar."},
   {"s":"Bake at 350°F for 30 minutes.","t":30},
   {"s":"Sprinkle with paprika before serving."}],
 "notes":[]
},
{
 "id":"chocolate-marshmallow-frosting","title":"Chocolate Marshmallow Frosting","cat":"Desserts",
 "card":"chocolate-marshmallow-frosting.jpg","back":"chocolate-marshmallow-frosting-back.jpg","cook":0,
 "facts":[["Cook","Stovetop, low heat"],["For","Angel food cake"]],
 "groups":[{"items":[
   {"q":2,"u":"square","i":"unsweetened chocolate","ge":28},
   {"q":2,"u":"tbsp","i":"butter"},
   {"q":1/3,"u":"cup","i":"evaporated milk","n":"“canned milk” on the card"},
   {"q":1,"u":"tsp","i":"vanilla"},
   {"q":3,"u":"cup","i":"powdered sugar","n":"sifted","gpc":120},
   {"q":0.5,"u":"bag","i":"miniature marshmallows","nus":"about 5 oz from a 10 oz bag","ge":283}]}],
 "steps":[
   {"s":"Melt the chocolate and butter in a saucepan over low heat."},
   {"s":"Remove from the heat. Add the evaporated milk and stir with a wooden spoon."},
   {"s":"Add the vanilla. Stir each time something is added."},
   {"s":"Gradually add the powdered sugar, stirring over low heat until it dissolves."},
   {"s":"Add the marshmallows and stir until they soften and just start to melt."},
   {"s":"Remove from the heat and frost the cake."}],
 "tips":["Do not use a mixer. It works better and is more manageable by stirring.",
         "The card says 1 Tbsp of vanilla, but 1 tsp is plenty."],
 "notes":[]
},
{
 "id":"potato-salad","title":"Potato Salad","cat":"Salads",
 "card":"potato-salad.jpg","cook":0,
 "facts":[["Cook","Boil"],["Serve","Cold or room temperature"]],
 "groups":[
   {"name":"Salad","items":[
     {"q":8,"i":"red potatoes"},
     {"q":5,"i":"eggs"},
     {"i":"salt and pepper"}]},
   {"name":"Dressing","items":[
     {"q":0.5,"u":"cup","i":"mayonnaise","gpc":220},
     {"q":2,"u":"tbsp","i":"cider vinegar"},
     {"q":0.25,"u":"tsp","i":"dry mustard"}]}],
 "steps":[
   {"s":"Boil the potatoes until soft. Hard-boil the eggs."},
   {"s":"Let the potatoes cool slightly, until you can handle them, then peel."},
   {"s":"Cut the potatoes into bite-size pieces."},
   {"s":"Peel and chop the eggs."},
   {"s":"Mix the mayonnaise, cider vinegar and dry mustard."},
   {"s":"Combine the potatoes and eggs with salt and pepper, then add the dressing until it tastes right."}],
 "notes":[]
},
{
 "id":"chinese-stir-fry","title":"Chinese Stir Fry","cat":"Mains",
 "card":"chinese-stir-fry.jpg","cook":10,
 "facts":[["Cook","Stovetop, medium-high"],["Serve","Over rice"]],
 "groups":[
   {"name":"Stir fry","items":[
     {"q":1,"q2":1.5,"u":"lb","i":"stir-fry beef","n":"leave in strips"},
     {"q":1,"u":"bag","i":"frozen Asian-style vegetable medley","n":"or veggies like peppers, broccoli, cauliflower"},
     {"q":1,"u":"tbsp","i":"water"},
     {"q":2,"u":"tbsp","i":"stir-fry sauce"},
     {"i":"cooking spray or canola oil"}]},
   {"name":"Rice","items":[
     {"q":1,"u":"cup","i":"Minute Rice","n":"follow box directions","gpc":95},
     {"q":1,"u":"cup","i":"water"}]}],
 "steps":[
   {"s":"Cook the rice according to the box directions."},
   {"s":"Heat a non-stick skillet over medium-high heat with cooking spray or canola oil."},
   {"s":"Cook the beef in the skillet for 2 minutes, stirring, until browned.","t":2},
   {"s":"Stir in the veggies and 1 tbsp water. Cook 1 minute while stirring.","t":1},
   {"s":"Stir in the stir-fry sauce until well mixed. Reduce the heat to medium, cover and cook 2–3 minutes, stirring frequently, until all the veggies are tender-crisp.","t":3},
   {"s":"Serve the beef over the rice."}],
 "notes":[]
},
{
 "id":"vegetable-beef-soup","title":"Vegetable-Beef Soup","cat":"Mains",
 "card":"vegetable-beef-soup.jpg","cook":360,
 "facts":[["Cook","Crockpot on high"],["Time","6 hr"],["Makes","quarts",6]],
 "groups":[
   {"items":[
     {"q":3,"u":"lb","i":"stew meat"},
     {"q":12,"u":"cup","i":"water","nus":"3 quarts"},
     {"q":1,"u":"can","i":"beef broth (Campbell's)","nus":"10.5 oz","ge":298},
     {"q":2,"u":"tbsp","i":"salt"},
     {"q":0.25,"u":"tsp","i":"pepper"},
     {"q":1,"i":"clove garlic, mashed"},
     {"q":1,"i":"medium onion, chopped"},
     {"q":1,"u":"bag","i":"frozen mixed vegetables"},
     {"q":1,"u":"can","i":"diced tomatoes","nus":"1 lb 12 oz (3½ cups)","ge":794},
     {"q":2,"u":"tsp","i":"parsley flakes"}]},
   {"name":"Optional add-ins","items":[
     {"q":1,"u":"cup","i":"frozen peas, corn and/or green beans","n":"1 cup of each you use","gpc":140},
     {"q":1/3,"u":"cup","i":"barley, regular rice or broken-up spaghetti","n":"instead of the extra vegetables","gpc":200}]}],
 "steps":[
   {"s":"Put the stew meat, water, beef broth, salt, pepper, garlic, onion, frozen mixed vegetables, tomatoes and parsley flakes in the crockpot."},
   {"s":"Cover and cook on high for 6 hours.","t":360},
   {"s":"Optional: add the frozen peas, corn or green beans just long enough before serving for them to cook tender. Or add the barley, rice or broken-up spaghetti instead."}],
 "notes":[]
},
{
 "id":"zucchini-bread","title":"Zucchini Bread","cat":"Breads & Sides",
 "card":"zucchini-bread.jpg","back":"zucchini-bread-back.jpg","cook":45,
 "facts":[["Oven","350°F"],["Bake","40 min +"],["Pan","9×5-inch loaf"]],
 "groups":[{"items":[
   {"q":1,"u":"cup","i":"presifted flour","gpc":115},
   {"q":1,"u":"tsp","i":"baking powder"},
   {"q":1,"u":"tsp","i":"baking soda"},
   {"i":"salt","n":"a pinch"},
   {"q":1.5,"u":"tsp","i":"cinnamon"},
   {"q":0.5,"u":"cup","i":"vegetable oil"},
   {"q":2,"i":"eggs"},
   {"q":1.5,"u":"cup","i":"shredded, unpeeled zucchini","gpc":125},
   {"q":1,"u":"tsp","i":"vanilla"},
   {"q":2,"u":"tbsp","i":"molasses"},
   {"q":2/3,"u":"cup","i":"sugar","gpc":200}]}],
 "steps":[
   {"s":"Blend the wet and dry ingredients separately, then mix them together in the mixing bowl."},
   {"s":"Blend all the ingredients at low speed until moistened, then beat at medium speed for 1 minute.","t":1},
   {"s":"Spread the batter in a 9×5-inch loaf pan sprayed with baking spray."},
   {"s":"Bake at 350°F. Check at 40 minutes, then about every 5 minutes until done.","t":40}],
 "tips":["Times on ovens seem to vary. Happy eating!"],
 "notes":[]
},
{
 "id":"cinnamon-toast","title":"Cinnamon Toast","cat":"Breads & Sides",
 "card":"cinnamon-toast.jpg","cook":4,
 "facts":[["Oven","400°F"],["Bake","3–4 min"]],
 "groups":[{"items":[
   {"i":"bread"},
   {"i":"butter, melted"},
   {"i":"cinnamon sugar","n":"1 part cinnamon to 6 parts sugar"}]}],
 "steps":[
   {"s":"Toast the bread in the toaster."},
   {"s":"Dip one side in the melted butter, then dip the buttered side in the cinnamon sugar."},
   {"s":"Place in a hot oven (400°F) for 3–4 minutes.","t":4}],
 "tips":["Crunchy taste treat."],
 "notes":[]
},
{
 "id":"neiman-marcus-cookies","title":"Neiman Marcus Chocolate Chip Cookies","cat":"Desserts",
 "fromline":"From Neiman Marcus",
 "card":"neiman-marcus-cookies.jpg","cook":20,
 "facts":[["Oven","300°F"],["Bake","About 20 min"],["Makes","cookies",24]],
 "groups":[{"items":[
   {"q":0.5,"u":"cup","i":"butter, softened","nus":"1 stick","gpc":227},
   {"q":1,"u":"cup","i":"light brown sugar","gpc":213},
   {"q":3,"u":"tbsp","i":"granulated sugar"},
   {"q":1,"i":"large egg"},
   {"q":2,"u":"tsp","i":"vanilla extract"},
   {"q":1.75,"u":"cup","i":"all-purpose flour","gpc":125},
   {"q":0.5,"u":"tsp","i":"baking powder"},
   {"q":0.5,"u":"tsp","i":"baking soda"},
   {"q":0.5,"u":"tsp","i":"salt"},
   {"q":1.5,"u":"tsp","i":"instant espresso powder"},
   {"q":1.5,"u":"cup","i":"semisweet chocolate chips","gpc":170}]}],
 "steps":[
   {"s":"Preheat the oven to 300°F."},
   {"s":"Cream the butter and both sugars with an electric mixer on medium speed until fluffy, about 30 seconds."},
   {"s":"Beat in the egg and vanilla for another 30 seconds."},
   {"s":"Sift the flour, baking powder, baking soda and salt together, then beat into the butter mixture on low speed for about 15 seconds."},
   {"s":"Stir in the espresso powder and chocolate chips."},
   {"s":"Drop 2-tablespoon scoops (a 1-ounce scoop) onto a greased cookie sheet about 3 inches apart. Press each down with the back of a spoon into a 2-inch circle."},
   {"s":"Bake about 20 minutes, until nicely browned around the edges. Bake a little longer for a crispier cookie.","t":20}],
 "notes":[]
},
{
 "id":"chicken-tortilla-casserole","title":"Chicken Tortilla Casserole","cat":"Mains",
 "card":"chicken-tortilla-casserole.jpg","cook":30,
 "facts":[["Oven","350°F"],["Bake","30 min"],["Dish","13×9 casserole"],["Serves","8–10"]],
 "groups":[{"items":[
   {"q":12,"i":"corn tortillas","n":"1 dozen"},
   {"q":1/3,"u":"cup","i":"oil","n":"for softening the tortillas"},
   {"q":1,"u":"tbsp","i":"instant onion"},
   {"q":0.5,"u":"cup","i":"milk"},
   {"q":1,"u":"can","i":"cream of chicken soup","nus":"10.5 oz","ge":298},
   {"q":1,"u":"can","i":"cream of mushroom soup","nus":"10.5 oz","ge":298},
   {"q":1,"u":"cup","i":"sour cream","gpc":240},
   {"q":3,"u":"tbsp","i":"diced green chiles"},
   {"q":0.5,"u":"tsp","i":"garlic salt"},
   {"q":2,"u":"cup","i":"canned chicken","gpc":140},
   {"q":0.5,"u":"lb","i":"Jack cheese, grated"},
   {"q":1,"u":"can","i":"chopped ripe olives"},
   {"i":"butter","n":"for greasing the dish"}]}],
 "steps":[
   {"s":"Grease a 13×9 casserole dish with butter."},
   {"s":"Heat the oil in a pan and soften the tortillas in it."},
   {"s":"Mix the onion, milk, both soups, sour cream, chiles and garlic salt."},
   {"s":"Layer in the dish: tortillas, chicken, soup mixture, olives, cheese. Repeat the layers."},
   {"s":"Bake at 350°F for 30 minutes.","t":30}],
 "notes":[]
},
{
 "id":"pecan-pie","title":"Pecan Pie","cat":"Desserts",
 "card":"pecan-pie.jpg","back":"pecan-pie-back.jpg","cook":55,
 "facts":[["Oven","350°F"],["Bake","35–55 min"],["Pie","9-inch"],["Serves","8"]],
 "groups":[{"items":[
   {"q":1,"i":"unbaked 9-inch pie shell"},
   {"q":3,"i":"eggs, slightly beaten"},
   {"q":1,"u":"cup","i":"white Karo (light corn syrup)","gpc":328},
   {"q":1,"u":"cup","i":"sugar","gpc":200},
   {"q":2,"u":"tbsp","i":"butter, melted"},
   {"q":2,"u":"tsp","i":"vanilla"},
   {"q":1.25,"u":"cup","i":"pecans","gpc":110}]}],
 "steps":[
   {"s":"Mix the eggs, Karo, sugar, butter and vanilla together."},
   {"s":"Break the pecans into pieces and put them in the pie shell."},
   {"s":"Pour the egg mixture over the pecans."},
   {"s":"Bake at 350°F for 35–55 minutes, until a knife inserted in the middle comes out almost clean. Start checking at 35.","t":55},
   {"s":"Cool."}],
 "tips":["This was the original Karo recipe!"],
 "notes":[]
},
{
 "id":"toasted-pumpkin-seeds","title":"Toasted Pumpkin Seeds","cat":"Snacks",
 "card":"toasted-pumpkin-seeds.jpg","cook":30,
 "facts":[["Oven","250–300°F"],["Toast","About 30 min"]],
 "groups":[{"items":[
   {"q":1,"u":"cup","i":"pumpkin seeds","gpc":130},
   {"q":1,"u":"tbsp","i":"butter, melted"},
   {"q":1,"u":"tsp","i":"salt"},
   {"q":0.125,"u":"tsp","i":"garlic powder","n":"optional"}]}],
 "steps":[
   {"s":"Wash the seeds and separate them from the pulp."},
   {"s":"Spread the seeds thinly on a baking sheet with the butter and salt (and garlic powder, if using)."},
   {"s":"Toast in a low oven, 250–300°F, for about 30 minutes, stirring occasionally, until crisp and brown.","t":30}],
 "tips":["The recipe I used when you were kids."],
 "notes":[]
},
{
 "id":"pignoli-cookies","title":"Pignoli Cookies","cat":"Desserts",
 "card":"pignoli-cookies.jpg","cook":14,
 "facts":[["Oven","350°F"],["Bake","12–14 min"],["Makes","5–6 dozen cookies"]],
 "groups":[{"items":[
   {"q":1.5,"u":"lb","i":"almond paste"},
   {"q":3,"u":"cup","i":"sugar","gpc":200},
   {"q":5,"q2":6,"i":"egg whites, beaten"},
   {"i":"vanilla","n":"a touch"},
   {"q":1,"u":"lb","i":"pignoli (pine) nuts"}]}],
 "steps":[
   {"s":"Line cookie sheets with parchment."},
   {"s":"Crumble the almond paste, then add the sugar, egg whites and a touch of vanilla."},
   {"s":"Blend together, by machine or by hand."},
   {"s":"Put the pignoli nuts in a bowl, about a quarter of the bag at a time."},
   {"s":"Wet your hands, roll the dough into small balls and roll each ball in the nuts until covered."},
   {"s":"Place on the cookie sheet and press down slightly to flatten a little."},
   {"s":"Bake at 350°F for 12–14 minutes. Watch your oven carefully.","t":14}],
 "tips":["I prefer the machine for blending."],
 "notes":[]
},
{
 "id":"lemon-lovelies","title":"Lemon Lovelies","cat":"Desserts",
 "card":"lemon-bars-sheet.jpg","cook":50,
 "facts":[["Oven","350°F"],["Bake","25 + 25 min"],["Pan","13×9-inch"]],
 "groups":[
   {"name":"Crust","items":[
     {"q":2,"i":"sticks butter","ge":113},
     {"i":"salt","n":"a pinch"},
     {"q":2,"u":"cup","i":"flour","gpc":125},
     {"q":0.5,"u":"cup","i":"powdered sugar","gpc":120}]},
   {"name":"Lemon layer","items":[
     {"q":4,"i":"eggs"},
     {"q":1,"i":"lemon, juice and grated rind","n":"about ½ cup juice"},
     {"q":2,"u":"cup","i":"sugar","gpc":200},
     {"q":4,"u":"tbsp","i":"flour"}]},
   {"name":"Topping","items":[{"i":"powdered sugar"}]}],
 "steps":[
   {"s":"Mix the butter, salt, flour and powdered sugar together and pat into a 13×9-inch pan."},
   {"s":"Bake at 350°F for 25 minutes.","t":25},
   {"s":"Meanwhile, mix the eggs, lemon juice and rind, sugar and flour, and beat for at least 1 minute."},
   {"s":"Pour over the hot crust and bake 25 minutes more at 350°F.","t":25},
   {"s":"Cool, sprinkle with powdered sugar and cut into squares."}],
 "notes":[]
},
{
 "id":"triple-layer-lemon-bars","title":"Triple Layer Lemon Bars","cat":"Desserts",
 "card":"lemon-bars-sheet.jpg","cook":40,
 "facts":[["Oven","325°F"],["Bake","30 + 30–40 min"],["Pan","8×8-inch"]],
 "groups":[
   {"name":"Shortbread crust","items":[
     {"q":0.5,"u":"cup","i":"butter","nus":"1 stick","gpc":227},
     {"q":0.25,"u":"cup","i":"powdered sugar","gpc":120},
     {"q":1,"u":"tsp","i":"vanilla"},
     {"q":1,"u":"cup","i":"flour","gpc":125}]},
   {"name":"Cream cheese filling","items":[
     {"q":8,"u":"oz","i":"cream cheese"},
     {"q":1.5,"u":"cup","i":"powdered sugar","gpc":120},
     {"q":1,"i":"egg"},
     {"q":1,"u":"tsp","i":"lemon extract"}]},
   {"name":"Lemon curd","items":[
     {"q":4,"i":"large egg yolks"},
     {"q":1,"u":"tbsp","i":"cornstarch"},
     {"q":0.75,"u":"cup","i":"white sugar","gpc":200},
     {"q":0.75,"u":"cup","i":"water"},
     {"q":2,"i":"medium lemons","n":"juiced, plus 2 tsp grated peel"},
     {"q":1,"u":"tbsp","i":"butter"}]},
   {"name":"Topping","items":[
     {"q":2,"u":"tbsp","i":"powdered sugar"}]}],
 "steps":[
   {"s":"Crust: cream the butter and powdered sugar, add the vanilla and mix, then add the flour and mix until fluffy."},
   {"s":"Press the dough into the bottom of an 8×8-inch pan and refrigerate 30 minutes.","t":30},
   {"s":"Prick the bottom and bake at 325°F for 30 minutes. Cool.","t":30},
   {"s":"Cream cheese filling: beat the cream cheese and powdered sugar, add the egg and lemon extract, and beat until light and smooth. Cover and refrigerate."},
   {"s":"Lemon curd: blend the egg yolks with the cornstarch and sugar. Over low heat, whisk in the water and lemon juice and cook until the mixture coats the back of a spoon."},
   {"s":"Remove from the heat, add the lemon peel and butter, and cool for 10 minutes.","t":10},
   {"s":"Spread the cream cheese filling over the crust, then spread the lemon curd over the cream cheese."},
   {"s":"Bake in the center of the oven at 325°F for 30–40 minutes.","t":40},
   {"s":"Cool, then chill in the refrigerator for 1 hour.","t":60},
   {"s":"Dust with the powdered sugar before serving.","added":True}],
 "tips":["A Mrs. Fields (supposedly) recipe. I haven't tried it, but it looks super."],
 "notes":[]
},
{
 "id":"chex-party-mix","title":"Original Chex Party Mix","cat":"Snacks",
 "card":"chex-party-mix.jpg","cook":6,
 "facts":[["Microwave","High"],["Cook","5–6 min"],["Makes","cups",10]],
 "groups":[{"items":[
   {"q":0.25,"u":"cup","i":"margarine or butter, melted","gpc":227},
   {"q":4.5,"u":"tsp","i":"Worcestershire sauce"},
   {"q":1.25,"u":"tsp","i":"seasoned salt"},
   {"q":8,"u":"cup","i":"Chex cereal","n":"Corn, Rice and/or Wheat","gpc":30},
   {"q":1,"u":"cup","i":"mixed nuts or peanuts","gpc":140},
   {"q":1,"u":"cup","i":"pretzels","gpc":45}]}],
 "steps":[
   {"s":"Mix the melted butter, Worcestershire sauce and seasoned salt."},
   {"s":"Put the cereal, nuts and pretzels in a large zipper bag. Pour the butter mixture over them, seal the bag and shake until everything is evenly coated."},
   {"s":"Tip into a large microwave-safe bowl. Microwave on High for 5–6 minutes, stirring well every 2 minutes and scraping the sides and bottom of the bowl. (These times were written for 625–700 watt microwaves, so start checking sooner in a stronger one.)","t":6},
   {"s":"Spread on paper towels to cool. Store in an airtight container."}],
 "notes":[]
},
{
 "id":"lasagne","title":"Lasagne","cat":"Mains",
 "card":"lasagne.jpg","cook":30,
 "facts":[["Oven","375°F"],["Bake","30 min"],["Dish","13×9 casserole"],["Serves","6–8"]],
 "groups":[
   {"name":"Meat sauce","items":[
     {"q":1,"u":"lb","i":"ground chuck"},
     {"q":1,"u":"tbsp","i":"olive oil"},
     {"q":1,"i":"clove garlic, minced"},
     {"q":1,"u":"tbsp","i":"parsley flakes"},
     {"q":1,"u":"tbsp","i":"basil"},
     {"q":2,"u":"tsp","i":"salt"},
     {"q":1,"u":"can","i":"whole peeled tomatoes","n":"large can","nus":"28 oz","ge":794},
     {"q":1,"u":"can","i":"tomato paste","nus":"6 oz","ge":170}]},
   {"name":"Cheese mixture","items":[
     {"q":24,"u":"oz","i":"cottage cheese","n":"three 8 oz cartons"},
     {"q":2,"i":"eggs, beaten"},
     {"q":1,"u":"tsp","i":"salt"},
     {"q":0.5,"u":"tsp","i":"pepper"},
     {"q":2,"u":"tbsp","i":"parsley flakes"},
     {"q":0.5,"u":"cup","i":"grated Parmesan cheese","n":"save a little for the top","gpc":100}]},
   {"name":"Also","items":[
     {"q":1,"u":"lb","i":"mozzarella cheese, grated"},
     {"q":1,"u":"package","i":"lasagne noodles","nus":"1 lb","ge":454}]}],
 "steps":[
   {"s":"Brown the ground chuck in the olive oil, then add the garlic, parsley, basil, salt, tomatoes and tomato paste. Simmer uncovered."},
   {"s":"Cook the noodles and rinse them in cold water."},
   {"s":"Combine the cottage cheese, eggs, salt, pepper, parsley and Parmesan (save a little Parmesan for the top)."},
   {"s":"In a 13×9 casserole dish, layer noodles, cottage cheese mixture, mozzarella and meat sauce. Repeat, then sprinkle the saved Parmesan on top."},
   {"s":"Bake at 375°F for 30 minutes.","t":30},
   {"s":"Let stand 10 minutes before serving.","t":10}],
 "tips":["Freezes well. Freezer to oven: cook 1 hr."],
 "notes":[]
},
{
 "id":"pollo-alla-milanese","title":"Pollo alla Milanese","sub":"Breaded Chicken Cutlets","cat":"Mains",
 "card":"pollo-alla-milanese.jpg","cook":15,
 "facts":[["Cook","Pan-fried"],["Serves","1 breast per person"]],
 "groups":[{"items":[
   {"i":"chicken breasts","n":"1 per person"},
   {"q":1,"i":"egg"},
   {"i":"salt"},
   {"i":"bread crumbs"},
   {"i":"vegetable oil"}]}],
 "steps":[
   {"s":"Butterfly the chicken breasts (open them up) and pound them thin."},
   {"s":"Put the egg and salt in a bowl and whip."},
   {"s":"Dip the breasts in the egg."},
   {"s":"Pour bread crumbs onto a plate and press both sides of each breast into them."},
   {"s":"Pour vegetable oil into a pan and fry the breasts. Turn when golden."},
   {"s":"When golden on both sides, lay them on paper towels."}],
 "notes":[]
},
{
 "id":"polpette","title":"Polpette","sub":"Meatballs","cat":"Mains",
 "card":"polpette.jpg","cook":30,
 "facts":[["Cook","about 30 min"],["Size","small fist"]],
 "groups":[{"items":[
   {"q":0.5,"u":"lb","i":"ground beef","n":"half of a 1 lb pack"},
   {"q":1,"i":"egg"},
   {"q":1,"u":"tbsp","i":"Parmesan cheese","n":"a spoonful"},
   {"i":"parsley"},
   {"q":2,"u":"slice","i":"bread","n":"soaked in milk or water, then squeezed"},
   {"i":"salt"},
   {"q":1,"u":"slice","i":"Black Forest ham, diced"},
   {"i":"bread crumbs"},
   {"i":"oil","n":"for frying"}]}],
 "steps":[
   {"s":"Soak the bread in milk or water, then squeeze it out."},
   {"s":"Mix the ground beef, egg, Parmesan, parsley, bread and salt."},
   {"s":"Add the diced ham, stir, then roll into meatballs the size of a small fist."},
   {"s":"Pour bread crumbs onto a plate and roll the polpette in them."},
   {"s":"Heat oil in a pan until hot enough to fry. Add the polpette and shake the pan."},
   {"s":"Cook slowly, making sure they cook on all sides, for about 30 minutes.","t":30}],
 "notes":[]
},
{
 "id":"gnocchi","title":"Gnocchi","sub":"Potato Dumplings","cat":"Mains",
 "card":"gnocchi.jpg","cook":5,
 "facts":[["Serves","",2]],
 "groups":[{"items":[
   {"q":1.5,"i":"big potatoes"},
   {"q":0.5,"u":"cup","i":"flour","n":"plus more while working the dough","gpc":125},
   {"i":"salt"}]}],
 "steps":[
   {"s":"Boil the potatoes, then mash them with ½ cup flour."},
   {"s":"Keep adding flour while working the dough. This must be done while it is still hot."},
   {"s":"Add salt and work the dough until it holds together."},
   {"s":"Cut the dough into big salami-like slices. Flour them and roll each one into a cylinder."},
   {"s":"Cut into small pieces, then run each piece along the side of a grater."},
   {"s":"Boil water and add salt. Drop in the gnocchi. They're ready when they float to the surface."}],
 "notes":[]
},
{
 "id":"peperoni-in-padella","title":"Peperoni in Padella","sub":"Pan-Cooked Peppers","cat":"Breads & Sides",
 "card":"peperoni-in-padella.jpg","cook":0,
 "facts":[["Cook","Slow, on the stove"]],
 "groups":[{"items":[
   {"q":3,"i":"bell peppers, sliced"},
   {"i":"oil"},
   {"i":"onion, diced"},
   {"q":0.5,"u":"cube","i":"bouillon (dado)"},
   {"i":"basil"}]}],
 "steps":[
   {"s":"Put the sliced peppers in a pan with the oil and diced onion. No water."},
   {"s":"Lay the peppers skin side down. Add the dado."},
   {"s":"Move the peppers from the sides of the pan to the center so they all cook."},
   {"s":"Add basil and cook slowly."}],
 "notes":[]
},
{
 "id":"zucchine-trifolate","title":"Zucchine Trifolate","sub":"Sautéed Zucchini","cat":"Breads & Sides",
 "card":"zucchine-trifolate.jpg","cook":20,
 "facts":[["Cook","about 20 min"],["Serves","",2]],
 "groups":[{"items":[
   {"q":5,"q2":6,"i":"zucchini"},
   {"q":1,"u":"slice","i":"onion"},
   {"i":"oil"},
   {"q":0.5,"u":"cube","i":"bouillon (dado)"}]}],
 "steps":[
   {"s":"Cut the zucchini in half lengthwise and remove part of the soft inside (only if it's soft). Cut into slices."},
   {"s":"Fry the onion in oil, but don't let it turn golden."},
   {"s":"Add the zucchini (don't add water) and stir. Add the dado."},
   {"s":"As they cook they will shrink, so lower the heat. Cook for about 20 minutes.","t":20}],
 "notes":[]
},
{
 "id":"lenticchie-lessate","title":"Lenticchie Lessate","sub":"Stewed Lentils","cat":"Breads & Sides",
 "card":"lenticchie-lessate.jpg","cook":20,
 "facts":[["Soak","4–6 hours"],["Cook","about 20 min"],["Serves","",2]],
 "groups":[{"items":[
   {"q":0.5,"u":"bag","i":"lentils","nus":"1 lb bag","ge":454},
   {"q":1,"u":"tbsp","i":"oil"},
   {"q":1,"u":"slice","i":"onion, diced"},
   {"i":"water","n":"enough to fill the pan halfway"},
   {"q":0.5,"u":"cube","i":"bouillon (dado)"},
   {"i":"salt"},
   {"q":1,"u":"tbsp","i":"tomato paste"},
   {"q":2,"i":"sage leaves"}]}],
 "steps":[
   {"s":"Soak the lentils in a small pot of lukewarm water for 4–6 hours."},
   {"s":"Sift through them and remove any bad ones or pebbles."},
   {"s":"Put the oil in a pan. Dice the onion slice and add it to the oil."},
   {"s":"Before the onion turns golden, add water to fill the pan halfway."},
   {"s":"Pour in the lentils. Add the dado, salt, tomato paste and sage leaves."},
   {"s":"Cover with a lid and cook for about 20 minutes.","t":20}],
 "notes":[]
},
{
 "id":"green-beans-almondine","title":"Green Beans Almondine","cat":"Breads & Sides",
 "card":"green-beans-almondine.jpg","cook":10,
 "facts":[["Cook","Stovetop, low heat"]],
 "groups":[{"items":[
   {"q":2,"u":"tbsp","i":"sliced almonds"},
   {"q":2,"u":"tbsp","i":"butter"},
   {"q":1,"u":"tsp","i":"lemon juice"},
   {"q":2,"u":"cup","i":"hot cooked green beans","gpc":125}]}],
 "steps":[
   {"s":"Melt the butter and add the almonds."},
   {"s":"Keep on low heat until the almonds look golden in color. Stir."},
   {"s":"Add the lemon juice."},
   {"s":"Pour over the hot cooked green beans."}],
 "notes":[]
},
{
 "id":"parmesan-yams","title":"Parmesan Yams","cat":"Breads & Sides",
 "card":"parmesan-yams.jpg","back":"parmesan-yams-back.jpg","cook":80,
 "facts":[["Oven","425°F"],["Bake","45–60 + 15–20 min"],["Pan","9-inch cake pan"]],
 "groups":[{"items":[
   {"q":2,"u":"lb","i":"yams"},
   {"q":1,"u":"stick","i":"butter","ge":113},
   {"q":0.5,"u":"cup","i":"Parmesan cheese","gpc":100},
   {"i":"salt and pepper"}]}],
 "steps":[
   {"s":"Peel the yams and slice them as thinly as possible."},
   {"s":"Melt the butter and put 2 tbsp in the bottom of a 9-inch cake pan."},
   {"s":"Put one layer of yams in the pan. Follow with 1 tbsp butter, a sprinkling of Parmesan, and salt and pepper to taste."},
   {"s":"Continue layering the same way, ending with cheese. There should be about 4–6 layers."},
   {"s":"Cover with a layer of wax paper or Saran wrap and press down. Remove the paper and replace it with foil."},
   {"s":"Bake at 425°F for 45 minutes to 1 hour.","t":45},
   {"s":"Remove the foil and continue baking for 15–20 minutes.","t":15}],
 "tips":["Check at 40 min. This baking time may be a little long."],
 "notes":[]
},
{
 "id":"crepes","title":"Crêpes","cat":"Breakfast",
 "card":"crepes.jpg","cook":0,
 "facts":[["Rest","30 min"],["Cook","Nonstick pan"]],
 "groups":[{"items":[
   {"q":1,"u":"cup","i":"milk","n":"¼ liter on the card"},
   {"q":1.4,"u":"cup","i":"flour","nus":"175 g","gpc":125},
   {"q":2,"i":"eggs"},
   {"q":2,"u":"tbsp","i":"sugar","n":"leave out for savory crêpes"},
   {"q":0.5,"u":"glass","i":"beer or white wine"},
   {"q":0.5,"u":"tbsp","i":"oil","n":"plus a drop for the pan"},
   {"q":1,"u":"pinch","i":"salt"}]}],
 "steps":[
   {"s":"Mix the ingredients together well. There should be no lumps."},
   {"s":"Let the batter rest for about 30 minutes.","t":30},
   {"s":"Heat a nonstick pan on the stove and grease it with a drop of oil (spread it with a piece of paper towel)."},
   {"s":"Pour in a small ladle of batter. Cook until the crêpe comes away from the pan, then flip it."}],
 "tips":["For savory crêpes: same ingredients, but without the sugar."],
 "notes":[]
},
]

# Recipes waiting on missing info.
# Pizza: Ali is checking whether there's a second "Pizza Crust ②" card. Card photos are in cards/on-hold/
# (pizza-crust-card1 + back, pizza-card2 + back). Agreed: one "Pizza" recipe; 1 tbsp olive oil total on the crusts.
# Mystery cake (batch 7): only the back of the card (9x13 cake, 350°F, brown-sugar glaze topping with nuts) —
# photo in cards/on-hold/mystery-cake-back.jpg. Waiting for the matching front card.
ON_HOLD = [
{
 "id":"pizza","title":"Pizza","cat":"Mains",
 "card":"on-hold/pizza-crust-card1.jpg","back":"on-hold/pizza-crust-card1-back.jpg","cook":20,
 "facts":[["Oven","425°F"],["Bake","20 min"],["Makes","pizzas",2]],
 "groups":[
   {"name":"Crust","items":[
     {"q":1,"u":"envelope","i":"dry yeast"},
     {"q":1,"u":"cup","i":"warm water"},
     {"q":4,"u":"cup","i":"flour","n":"¼ cup set aside","gpc":125},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"q":0.25,"u":"tsp","i":"pepper"},
     {"q":2,"u":"tbsp","i":"olive oil"},
     {"q":1,"u":"tbsp","i":"olive oil","n":"for the crusts, plus more for the pans"}]},
   {"name":"Sauce","items":[
     {"q":16,"u":"oz","i":"can tomato sauce"},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"q":0.5,"u":"tsp","i":"oregano"},
     {"q":0.25,"u":"tsp","i":"pepper"},
     {"q":1,"i":"clove garlic, crushed"}]},
   {"name":"Toppings","items":[{"i":"toppings","n":"as desired"}]}],
 "steps":[
   {"s":"Dissolve the yeast in the warm water."},
   {"s":"Sift the flour into a bowl. Remove and reserve ¼ cup of it. Add the salt and pepper."},
   {"s":"Make a well in the center of the bowl. Pour in the dissolved yeast and 2 tbsp olive oil. Work this gradually into the flour and knead into a ball."},
   {"s":"Sprinkle the top with the reserved ¼ cup flour. Cover and let rise at least 2 hours.","t":120},
   {"s":"Knead the dough and divide it in half."},
   {"s":"Oil the pizza pans with olive oil and roll out the dough. Drizzle the 1 tbsp olive oil over the crusts."},
   {"s":"Stir the sauce ingredients together and spread half on each pizza. Add desired toppings."},
   {"s":"Bake at 425°F for 20 minutes.","t":20}],
 "notes":[]
},
]

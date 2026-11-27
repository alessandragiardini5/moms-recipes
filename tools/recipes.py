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
{
 "id":"roll-out-cookies","title":"Roll-Out Cookies","cat":"Desserts",
 "card":"roll-out-cookies.jpg","cook":7,
 "facts":[["Oven","400°F"],["Bake","6–7 min"],["Makes","20–24 cookies"]],
 "groups":[{"items":[
   {"q":1,"u":"cup","i":"butter","nus":"2 sticks","gpc":227},
   {"q":1,"u":"cup","i":"sugar","gpc":200},
   {"q":1,"i":"large egg"},
   {"q":1,"u":"tsp","i":"vanilla"},
   {"q":2,"u":"tsp","i":"baking powder"},
   {"q":3,"u":"cup","i":"flour","gpc":125}]}],
 "steps":[
   {"s":"Preheat the oven to 400°F."},
   {"s":"In a large bowl, cream the butter and sugar with an electric mixer. Beat in the egg and vanilla."},
   {"s":"Mix the baking powder into the flour. Add it one cup at a time, mixing after each addition."},
   {"s":"The dough will be very stiff, so blend in the last of the flour by hand. If it gets too stiff, add water a teaspoon at a time. Don't chill the dough."},
   {"s":"Divide the dough into 2 balls. On a floured surface, roll each one into a circle about 12 inches across and ⅛ inch thick."},
   {"s":"Dip the cutters in flour before each cut. Place the cookies on an ungreased cookie sheet."},
   {"s":"Bake on the top rack for 6–7 minutes, until lightly browned.","t":7}],
 "tips":["Colored cookies: tint the dough with icing color, adding a little at a time until you get the color you want.",
         "Chocolate cookies: stir 3 oz melted unsweetened chocolate into the dough."],
 "notes":[]
},
{
 "id":"piecrust-shortcakes","title":"Piecrust Shortcakes","cat":"Desserts",
 "card":"piecrust-shortcakes.jpg","cook":12,
 "facts":[["Oven","350°F"],["Bake","10–12 min"],["Makes","9 rounds per piecrust"]],
 "groups":[
   {"name":"Pastry rounds","items":[
     {"i":"refrigerated piecrusts","n":"the rolled kind, like Pillsbury"},
     {"i":"egg, lightly beaten"},
     {"i":"white sparkling sugar or granulated sugar"}]},
   {"name":"Filling","items":[
     {"i":"fresh fruit, sliced","n":"e.g. nectarines and strawberries"},
     {"i":"berries","n":"e.g. blueberries and raspberries"},
     {"i":"granulated sugar"},
     {"i":"whipped cream"},
     {"i":"fresh mint","n":"for garnish, optional"}]}],
 "steps":[
   {"s":"Unroll the piecrust on a lightly floured surface and cut out circles with a 3-inch round cutter (about 9 per crust, a few more if you reroll the scraps)."},
   {"s":"Brush the top of each circle with beaten egg and sprinkle with sugar. Arrange on ungreased baking sheets."},
   {"s":"Bake at 350°F for 10–12 minutes, until golden brown.","t":12},
   {"s":"Cool completely on wire racks."},
   {"s":"Toss the fruit and berries with a little sugar. Layer the pastry rounds with the fruit and a generous spoonful of whipped cream."}],
 "tips":["Almost any mix of seasonal fruit works."],
 "notes":[]
},
{
 "id":"lemon-ricotta-cookies","title":"Lemon Ricotta Cookies","cat":"Desserts",
 "card":"lemon-ricotta-cookies.jpg","back":"lemon-ricotta-cookies-back.jpg","cook":15,
 "facts":[["Oven","350°F"],["Bake","12–15 min"],["Makes","about 4 dozen"]],
 "groups":[
   {"name":"Cookies","items":[
     {"q":1,"u":"cup","i":"unsalted butter, softened","nus":"2 sticks","gpc":227},
     {"q":2,"u":"cup","i":"granulated sugar","gpc":200},
     {"q":2,"i":"large eggs"},
     {"q":15,"u":"oz","i":"whole milk ricotta cheese"},
     {"q":0.5,"u":"tsp","i":"lemon extract","n":"or 1 tsp lemon and/or tangerine baking oil"},
     {"q":3,"u":"tbsp","i":"Meyer lemon zest, freshly grated"},
     {"q":1,"u":"tbsp","i":"Meyer lemon juice"},
     {"q":2.5,"u":"cup","i":"all-purpose flour","gpc":125},
     {"q":1,"u":"tsp","i":"baking powder"},
     {"q":1,"u":"tsp","i":"salt"}]},
   {"name":"Glaze","items":[
     {"q":6,"u":"tbsp","i":"unsalted butter","nus":"¾ stick"},
     {"q":3,"u":"cup","i":"confectioners' sugar","gpc":120},
     {"q":3,"q2":4,"u":"tbsp","i":"Meyer lemon juice"},
     {"i":"decorating sugar or silver dragées","n":"optional"}]}],
 "steps":[
   {"s":"Preheat the oven to 350°F and line baking sheets with parchment paper."},
   {"s":"Cream the butter and sugar until light and fluffy. Add the eggs, ricotta, lemon extract (or baking oil), zest and juice, and blend well."},
   {"s":"Add 1 cup of the flour with the baking powder and salt and blend. Add the rest of the flour in two parts, blending in between, until a dough forms."},
   {"s":"Drop rounded tablespoons of dough 2 inches apart onto the baking sheets."},
   {"s":"Bake 12–15 minutes, until the edges are very lightly golden.","t":15},
   {"s":"Let the cookies rest on the sheet for a few minutes, then move them to a wire rack."},
   {"s":"While they cool, make the glaze: cream the butter and confectioners' sugar, then keep mixing while you add the lemon juice a little at a time until it's the consistency you want."},
   {"s":"Glaze the cooled cookies and add dragées or decorating sugar, if you like, before the icing sets."}],
 "tips":["Meyer lemons are in specialty stores from mid-November to early spring. You'll need 2–3 medium lemons. Regular lemons work too."],
 "notes":[]
},
{
 "id":"moms-chili","title":"Mom's Chili","cat":"Mains",
 "card":"moms-chili.jpg","cook":30,
 "facts":[["Soak","Beans overnight"],["Simmer","30 min"],["Serves","A big pot"]],
 "groups":[{"items":[
   {"q":1,"u":"lb","i":"pink beans"},
   {"q":1,"u":"tbsp","i":"salt","n":"for the bean water, plus more to taste"},
   {"q":2,"q2":3,"u":"strip","i":"bacon","n":"or salt pork, for the beans"},
   {"q":1,"i":"onion, quartered"},
   {"q":2,"u":"lb","i":"ground beef"},
   {"i":"bacon drippings"},
   {"q":3,"i":"cloves garlic, minced"},
   {"q":2,"u":"tsp","i":"ground cumin","n":"optional"},
   {"q":1,"u":"tsp","i":"oregano"},
   {"q":1,"u":"can","i":"diced green chiles","n":"small can"},
   {"q":2,"u":"tbsp","i":"chili powder"},
   {"q":1,"u":"tbsp","i":"chili con carne seasoning"},
   {"q":1.5,"u":"tbsp","i":"flour"},
   {"q":1,"u":"can","i":"tomato sauce","n":"small can"},
   {"q":1,"u":"can","i":"peeled tomatoes","n":"large can; may not need the juice"},
   {"q":1,"u":"tbsp","i":"vinegar"}]}],
 "steps":[
   {"s":"Soak the beans overnight."},
   {"s":"Cook the beans in 1 quart of salted water with the bacon (or salt pork) and the onion until tender. Add water if they start to dry out, and keep adding salt to taste."},
   {"s":"Meanwhile, brown the meat in bacon drippings. Drain the grease as needed, leaving some to keep the meat moist."},
   {"s":"Add the garlic, cumin, oregano, green chiles, chili powder and chili con carne seasoning. Mix well."},
   {"s":"Remove from the heat. Add the tomatoes, tomato sauce, flour and vinegar, mixing well."},
   {"s":"Pour the mixture into the drained beans and simmer for 30 minutes.","t":30},
   {"s":"Serve topped with chopped onions, with crackers on the side."}],
 "notes":[]
},
{
 "id":"layered-seafood-spread","title":"Layered Seafood Spread","cat":"Appetizers",
 "card":"layered-seafood-spread.jpg","cook":5,
 "facts":[["Chill","At least 30 min, then until cold"],["Serves","appetizer servings",25]],
 "groups":[{"items":[
   {"q":2.5,"u":"cup","i":"water"},
   {"q":0.75,"u":"lb","i":"unpeeled medium-size fresh shrimp"},
   {"q":1,"u":"package","i":"cream cheese, softened","nus":"8 oz","ge":227},
   {"q":0.25,"u":"cup","i":"lemon juice"},
   {"q":1,"u":"tbsp","i":"mayonnaise"},
   {"q":0.5,"u":"tsp","i":"seasoned salt"},
   {"q":0.5,"u":"tsp","i":"lemon-pepper seasoning"},
   {"q":0.25,"u":"tsp","i":"Worcestershire sauce"},
   {"q":1,"u":"jar","i":"cocktail sauce","nus":"12 oz","ge":340},
   {"q":2,"u":"cup","i":"shredded Monterey Jack cheese","nus":"8 oz","gpc":113},
   {"q":3,"i":"green onions, chopped"},
   {"q":0.5,"u":"cup","i":"chopped green pepper","gpc":75},
   {"q":0.5,"u":"cup","i":"sliced ripe olives","gpc":70},
   {"i":"assorted crackers","n":"for serving"}]}],
 "steps":[
   {"s":"Bring the water to a boil, add the shrimp and cook 3–5 minutes.","t":5},
   {"s":"Drain, rinse with cold water and chill. Peel and devein. Chop half the shrimp and chill both the chopped and whole shrimp."},
   {"s":"Beat the cream cheese with an electric mixer on medium until light and fluffy. Add the lemon juice, mayonnaise, seasoned salt, lemon-pepper seasoning and Worcestershire, and beat until smooth."},
   {"s":"Spread into a 10-inch circle on a large serving platter. Cover and chill at least 30 minutes.","t":30},
   {"s":"Spread the cocktail sauce evenly over the cream cheese. Layer the chopped shrimp, Monterey Jack, green onions, green pepper and olives on top, then finish with the whole shrimp."},
   {"s":"Cover and chill thoroughly. Serve with assorted crackers."}],
 "notes":[]
},
{
 "id":"macaroni-salad","title":"Macaroni Salad","cat":"Salads",
 "card":"macaroni-salad.jpg","back":"macaroni-salad-back.jpg","cook":0,
 "facts":[["Chill","Overnight"]],
 "groups":[
   {"name":"Salad","items":[
     {"q":1,"u":"lb","i":"salad macaroni"},
     {"q":12,"i":"large green onion (chive) stems, chopped"},
     {"q":4,"i":"hard-boiled eggs, chopped"},
     {"q":1,"u":"cup","i":"chopped celery","gpc":100},
     {"q":12,"u":"slice","i":"crisp bacon, crumbled"},
     {"q":1,"u":"jar","i":"pimentos","nus":"4 oz","ge":113},
     {"q":1,"u":"cup","i":"chopped sweet pickles","gpc":150}]},
   {"name":"Dressing","items":[
     {"q":1.5,"u":"cup","i":"mayonnaise","gpc":220},
     {"q":1,"u":"tbsp","i":"horseradish"},
     {"q":2,"u":"tsp","i":"mustard"},
     {"q":1,"u":"tbsp","i":"pickle juice"},
     {"i":"salt and pepper"}]}],
 "steps":[
   {"s":"Cook the macaroni according to the package, drain, rinse with cold water and let it cool."},
   {"s":"Mix the mayonnaise, horseradish, mustard and pickle juice, and season with salt and pepper."},
   {"s":"Combine the macaroni with the green onions, eggs, celery, bacon, pimentos and pickles. Stir in the dressing."},
   {"s":"Chill overnight."}],
 "notes":[]
},
{
 "id":"caramel-apples","title":"Caramel Apples","cat":"Desserts",
 "card":"caramel-apples.jpg","cook":0,
 "facts":[["Microwave","About 3 min"],["Chill","45 min"],["Serves","6–8"]],
 "groups":[{"items":[
   {"q":48,"i":"caramels","n":"one 14-oz package"},
   {"q":2,"u":"tbsp","i":"water"},
   {"q":6,"q2":8,"i":"apples, washed, dried and stems removed"},
   {"q":6,"q2":8,"i":"wooden craft sticks"}]}],
 "steps":[
   {"s":"Put the caramels and water in a large microwave-safe bowl. Microwave on High for 2 minutes, then stir.","t":2},
   {"s":"Keep microwaving on High in 20–30 second bursts, stirring, until smooth."},
   {"s":"Push a craft stick into the stem end of each apple. Dip in the melted caramel and scrape the excess off the bottom."},
   {"s":"Set the apples on a greased, waxed-paper-lined tray. Chill 45 minutes, or until set.","t":45}],
 "tips":["If the caramel gets firm, microwave it again for 20–30 seconds until it's dippable.",
         "Decorating ideas: roll warm apples in chopped pecans and drizzle with melted chocolate.",
         "Press nonpareil-covered chocolate chips onto warm apples and drizzle with melted white chocolate.",
         "Roll warm apples in chopped multicolored chocolate candies.",
         "Roll warm apples in graham cracker pieces and mini marshmallows, then drizzle with melted chocolate.",
         "Drizzle cooled apples with melted white and dark chocolate.",
         "Wrap chewy fruit strips around the apple like a big bow.",
         "Make a baseball: cover a cooled apple in melted white chocolate and pipe on the stitches with dark chocolate."],
 "notes":[]
},
{
 "id":"spritzkransar","title":"Spritzkransar","sub":"Swedish Sugar Cookies","cat":"Desserts",
 "card":"spritzkransar.jpg","cook":10,
 "facts":[["Oven","350°F"],["Bake","10 min"],["Tool","Cookie press"]],
 "groups":[{"items":[
   {"q":0.5,"u":"lb","i":"butter or margarine, softened"},
   {"q":1,"u":"cup","i":"sugar","gpc":200},
   {"q":1,"i":"egg"},
   {"q":2.5,"u":"cup","i":"presifted flour","gpc":125},
   {"q":1,"u":"tsp","i":"baking powder"},
   {"q":0.5,"u":"tsp","i":"almond flavoring"}]}],
 "steps":[
   {"s":"Cream the butter and sugar together. Add the egg and almond flavoring."},
   {"s":"Mix the baking powder into the flour, then gradually add it to make a soft cookie dough."},
   {"s":"Press through a cookie press."},
   {"s":"Bake at 350°F for 10 minutes, or until very light brown.","t":10}],
 "notes":[]
},
{
 "id":"julies-oatmeal-cookies","title":"Julie's Oatmeal Cookies","cat":"Desserts",
 "card":"julies-oatmeal-cookies.jpg","cook":15,
 "facts":[["Oven","350°F"],["Bake","12–15 min"],["Makes","dozen",2.5]],
 "groups":[{"items":[
   {"q":0.75,"u":"cup","i":"butter or margarine","gpc":227},
   {"q":1,"u":"cup","i":"brown sugar","gpc":200},
   {"q":0.25,"u":"cup","i":"white sugar","gpc":200},
   {"q":1,"i":"egg"},
   {"q":1,"u":"tsp","i":"vanilla"},
   {"q":0.25,"u":"cup","i":"water"},
   {"q":2.5,"u":"cup","i":"oats","gpc":90},
   {"q":0.75,"u":"cup","i":"flour","n":"plus 1 tablespoon","gpc":125},
   {"q":2,"u":"tbsp","i":"unprocessed bran (not bran cereal)","n":"optional"},
   {"q":0.5,"u":"tsp","i":"baking soda"},
   {"q":1,"u":"tsp","i":"cinnamon"},
   {"q":0.25,"u":"tsp","i":"ground cloves"},
   {"q":1,"u":"cup","i":"diced walnuts","gpc":120},
   {"q":1,"u":"cup","i":"raisins","gpc":150},
   {"q":0.5,"u":"cup","i":"shredded coconut","n":"optional","gpc":85}]}],
 "steps":[
   {"s":"Cream the butter and sugars (an electric mixer works well)."},
   {"s":"Add the egg, water and vanilla."},
   {"s":"Combine the flour, bran, baking soda, cinnamon and cloves, and stir into the butter mixture."},
   {"s":"Add the oats, nuts, raisins and coconut."},
   {"s":"Bake at 350°F for 12–15 minutes, until light golden brown.","t":15}],
 "tips":["If you like a soft, chewy cookie, always underbake them a little — they should be light golden brown. If you like a crispy cookie, leave them in until darker in color.","This recipe only makes about 2½ dozen."],
 "notes":[]
},
{
 "id":"bisquick-strawberry-shortcakes","title":"Strawberry Shortcakes","cat":"Desserts",
 "fromline":"From Bisquick",
 "card":"bisquick-strawberry-shortcakes.jpg","cook":12,
 "facts":[["Oven","425°F"],["Bake","10–12 min"],["Makes","shortcakes",6]],
 "groups":[{"items":[
   {"q":4,"u":"cup","i":"sliced strawberries","nus":"1 qt","gpc":166},
   {"q":0.5,"u":"cup","i":"sugar","gpc":200},
   {"q":7/3,"u":"cup","i":"Original Bisquick","gpc":120},
   {"q":0.5,"u":"cup","i":"milk"},
   {"q":3,"u":"tbsp","i":"sugar"},
   {"q":3,"u":"tbsp","i":"butter or margarine, melted"},
   {"q":1,"u":"tub","i":"Cool Whip, thawed","nus":"8 oz","ge":227}]}],
 "steps":[
   {"s":"Mix the strawberries with the ½ cup sugar and set aside."},
   {"s":"Heat the oven to 425°F. Stir the Bisquick, milk, 3 tbsp sugar and melted butter until a soft dough forms."},
   {"s":"Drop the dough in 6 spoonfuls onto an ungreased cookie sheet."},
   {"s":"Bake 10–12 minutes, until golden brown.","t":12},
   {"s":"Split the warm shortcakes; fill and top with the strawberries and Cool Whip."}],
 "tips":["High altitude: heat the oven to 450°F and use 1 tbsp sugar in the dough."],
 "notes":[]
},
{
 "id":"pie-crust","title":"Pie Crust","cat":"Desserts",
 "card":"pie-crust.jpg","back":"pie-crust-back.jpg","cook":0,
 "facts":[["Makes","10-inch two-crust pie"],["Serves","8–10"]],
 "groups":[{"items":[
   {"q":3,"u":"cup","i":"sifted flour","gpc":115},
   {"q":1.5,"u":"tsp","i":"salt"},
   {"q":1,"u":"cup","i":"shortening","n":"plus 2 tbsp","gpc":190},
   {"q":6,"u":"tbsp","i":"ice water"}]}],
 "steps":[
   {"s":"Sift the flour and add the salt."},
   {"s":"Using a pastry blender, mix in the shortening until it is well blended."},
   {"s":"Add the ice water 1 tbsp at a time, stirring with a fork until blended each time you add water."},
   {"s":"Gather the dough into one large ball and cut it in half."},
   {"s":"Roll out on a pastry cloth, using a stockinette on the rolling pin."}],
 "notes":[]
},
{
 "id":"moms-famous-coffee-cake","title":"Mom's Famous Coffee Cake","cat":"Desserts",
 "card":"moms-famous-coffee-cake.jpg","back":"moms-famous-coffee-cake-back.jpg","cook":50,
 "facts":[["Oven","350°F"],["Bake","40–50 min"],["Pan","Bundt"],["Serves","8–10"]],
 "groups":[
   {"name":"Cake","items":[
     {"q":1.5,"u":"stick","i":"butter or margarine","ge":113},
     {"q":1.25,"u":"cup","i":"sugar","gpc":200},
     {"q":2,"i":"eggs"},
     {"q":1,"u":"cup","i":"sour cream","nus":"½ pint","gpc":240},
     {"q":1,"u":"tsp","i":"vanilla"},
     {"q":2,"u":"cup","i":"sifted flour","gpc":115},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"q":1,"u":"tsp","i":"baking powder"},
     {"q":0.5,"u":"tsp","i":"baking soda"}]},
   {"name":"Topping","items":[
     {"q":0.5,"u":"cup","i":"finely chopped pecans or walnuts","gpc":115},
     {"q":2,"u":"tbsp","i":"sugar"},
     {"q":1,"u":"tsp","i":"cinnamon"}]}],
 "steps":[
   {"s":"Cream together the butter and sugar."},
   {"s":"Add the eggs, sour cream and vanilla. Beat well."},
   {"s":"Add the flour, salt, baking powder and baking soda. Blend with a mixer until smooth."},
   {"s":"Mix the topping ingredients together."},
   {"s":"Layer in a greased and floured bundt pan: half the topping, half the batter, the rest of the topping, the rest of the batter."},
   {"s":"Bake at 350°F for 40–50 minutes.","t":50},
   {"s":"Cool. Remove from the pan."}],
 "tips":["Happy Eating!"],
 "notes":[]
},
{
 "id":"strawberry-meringue-cake","title":"Strawberry Meringue Cake","cat":"Desserts",
 "card":"strawberry-meringue-cake.jpg","back":"strawberry-meringue-cake-back.jpg","cook":40,
 "facts":[["Oven","350°F"],["Bake","35–40 min"],["Pans","Two 9×9"]],
 "groups":[
   {"name":"Cake","items":[
     {"q":1,"u":"package","i":"yellow cake mix","n":"no pudding in mix"},
     {"q":1,"u":"cup","i":"orange juice"},
     {"q":1/3,"u":"cup","i":"water"},
     {"q":4,"i":"egg yolks"},
     {"q":1,"u":"tsp","i":"grated orange peel"}]},
   {"name":"Meringue","items":[
     {"q":4,"i":"egg whites"},
     {"q":0.25,"u":"tsp","i":"cream of tartar"},
     {"q":1,"u":"cup","i":"sugar","gpc":200}]},
   {"name":"Filling","items":[
     {"q":3,"u":"pint","i":"strawberries","n":"3 boxes"},
     {"q":2,"u":"cup","i":"heavy (whipping) cream","nus":"1 pint"},
     {"q":0.25,"u":"cup","i":"sugar","gpc":200}]}],
 "steps":[
   {"s":"Combine the cake mix, orange juice, water, egg yolks and orange peel. Beat 4 minutes with a mixer."},
   {"s":"Pour into two greased, waxed-paper-lined 9×9 pans."},
   {"s":"Beat the egg whites with the cream of tartar to soft peaks. Slowly add the 1 cup sugar, beating to stiff peaks. Gently spread the meringue over the batter."},
   {"s":"Bake at 350°F for 35–40 minutes. Cool.","t":40},
   {"s":"Carefully remove the layers from the pans, keeping the meringue side on top."},
   {"s":"Save a few berries for garnish and slice the rest."},
   {"s":"Whip the cream with the ¼ cup sugar."},
   {"s":"Spread ⅔ of the whipped cream over the meringue on the bottom layer. Arrange the sliced berries on the cream."},
   {"s":"Add the top layer, meringue side up. Garnish with the remaining whipped cream and the whole berries."}],
 "tips":["Or spread the cream and add the berries on a single layer."],
 "notes":[]
},
{
 "id":"julies-chocolate-chip-coffee-cake","title":"Julie's Chocolate Chip Coffee Cake","cat":"Desserts",
 "card":"julies-chocolate-chip-coffee-cake.jpg","back":"julies-chocolate-chip-coffee-cake-back.jpg","cook":60,
 "facts":[["Oven","350°F"],["Bake","1 hr"],["Pan","Bundt"]],
 "groups":[
   {"name":"Cake","items":[
     {"q":1,"u":"package","i":"Duncan Hines yellow cake mix"},
     {"q":1,"u":"package","i":"vanilla instant pudding","n":"small"},
     {"q":4,"i":"eggs"},
     {"q":1,"u":"carton","i":"sour cream","n":"small"},
     {"q":0.25,"u":"cup","i":"milk"},
     {"q":0.5,"u":"cup","i":"Crisco oil"}]},
   {"name":"Swirl","items":[
     {"q":0.5,"u":"cup","i":"sugar","gpc":200},
     {"q":3,"u":"tbsp","i":"Hershey's baking cocoa"},
     {"q":1,"u":"tbsp","i":"brown sugar"},
     {"q":0.5,"u":"tsp","i":"cinnamon"},
     {"q":1,"u":"package","i":"chocolate chips","n":"small"}]}],
 "steps":[
   {"s":"In a large mixing bowl combine the cake mix, pudding, eggs, sour cream, milk and oil. Beat with a mixer for 8 minutes.","t":8},
   {"s":"Mix the sugar, cocoa, brown sugar and cinnamon in a small bowl."},
   {"s":"Pour half the batter into a greased bundt pan. Sprinkle with a little more than half the sugar mixture, then sprinkle the chocolate chips over it."},
   {"s":"Add the remaining batter, then the remaining sugar mixture. Cut through with a knife and swirl gently."},
   {"s":"Bake at 350°F for 1 hour, or until a tester comes out clean.","t":60},
   {"s":"Cool in the pan for 20 minutes, then turn out onto a platter or cake holder.","t":20}],
 "notes":[]
},
{
 "id":"pumpkin-bread","title":"Pumpkin Bread","cat":"Breads & Sides",
 "card":"pumpkin-bread.jpg","back":"pumpkin-bread-back.jpg","cook":60,
 "facts":[["Oven","350°F"],["Bake","45–60 min"],["Makes","2 large loaves or 3 coffee-can loaves"]],
 "groups":[
   {"name":"Combine","items":[
     {"q":1,"u":"cup","i":"vegetable oil"},
     {"q":4,"i":"eggs, beaten"},
     {"q":2/3,"u":"cup","i":"water"},
     {"q":2,"u":"cup","i":"pumpkin","nus":"1 small can","gpc":245}]},
   {"name":"Sift together","items":[
     {"q":10/3,"u":"cup","i":"flour","gpc":125},
     {"q":2,"u":"tsp","i":"baking soda"},
     {"q":1.5,"u":"tsp","i":"salt"},
     {"q":1,"u":"tsp","i":"cinnamon"},
     {"q":1,"u":"tsp","i":"nutmeg"},
     {"q":3,"u":"cup","i":"sugar","gpc":200}]},
   {"name":"Stir in","items":[
     {"q":0.75,"u":"cup","i":"currants","gpc":145},
     {"q":0.5,"u":"cup","i":"chopped pecans","gpc":115}]}],
 "steps":[
   {"s":"Combine the oil, eggs, water and pumpkin."},
   {"s":"Sift together the flour, baking soda, salt, cinnamon, nutmeg and sugar."},
   {"s":"Make a well in the center of the dry ingredients and add the pumpkin mixture. Blend well with a mixer."},
   {"s":"Stir in the currants and chopped pecans."},
   {"s":"Grease and flour the pans (2 large loaf pans or 3 one-pound coffee cans)."},
   {"s":"Bake at 350°F for 45–60 minutes.","t":60}],
 "notes":[]
},
{
 "id":"mitten-sugar-cookies","title":"Donna Monaco Olsen's \"Mitten\" Sugar Cookies","cat":"Desserts",
 "card":"mitten-sugar-cookies.jpg","cook":10,
 "facts":[["Oven","350°F"],["Bake","8–10 min"],["Chill","at least 2 hours"],["Makes","24–30 cookies"]],
 "groups":[{"items":[
   {"q":0.5,"u":"cup","i":"butter","gpc":227},
   {"q":1,"u":"cup","i":"sugar","gpc":200},
   {"q":1,"i":"egg"},
   {"q":1.75,"u":"cup","i":"flour","gpc":125},
   {"q":1,"u":"tsp","i":"baking powder"},
   {"q":1,"u":"tbsp","i":"milk"},
   {"q":0.5,"u":"tsp","i":"vanilla extract"},
   {"q":0.25,"u":"tsp","i":"salt"}]}],
 "steps":[
   {"s":"Cream the butter and sugar, then mix in the egg."},
   {"s":"Add all the other ingredients and mix until smooth. Do not overmix."},
   {"s":"Refrigerate the dough at least 2 hours. (It's okay to freeze it and then thaw it in the refrigerator.)","t":120},
   {"s":"Heat the oven to 350°F. Roll out the dough and cut with cookie cutters."},
   {"s":"Bake 8–10 minutes, or until lightly browned on the edges.","t":10},
   {"s":"Cool on a rack."}],
 "tips":["Fill with jam and sandwich together, or put sprinkles or sugar on top.","Makes 24–30 cookies depending on the size of the cutters.","Cookies freeze well. Enjoy!"],
 "notes":[]
},
{
 "id":"lemon-kiss-cookies","title":"Lemon Kiss Cookies","cat":"Desserts",
 "card":"lemon-kiss-cookies.jpg","cook":12,
 "facts":[["Oven","375°F"],["Bake","8–12 min"],["Chill","1 hour"]],
 "groups":[
   {"name":"Cookies","items":[
     {"q":1.5,"u":"cup","i":"butter or oleo, softened","gpc":227},
     {"q":0.75,"u":"cup","i":"sugar","gpc":200},
     {"q":1,"u":"tbsp","i":"lemon extract"},
     {"q":2.75,"u":"cup","i":"flour","gpc":125},
     {"q":1.5,"u":"cup","i":"finely chopped almonds","gpc":115},
     {"q":1,"u":"bag","i":"Hershey's Kisses","nus":"14 oz","ge":397}]},
   {"name":"Topping","items":[
     {"i":"powdered sugar"},
     {"q":0.5,"u":"cup","i":"semi-sweet chocolate chips","gpc":170},
     {"q":1,"u":"tbsp","i":"shortening"}]}],
 "steps":[
   {"s":"Beat the butter, sugar and lemon extract until fluffy."},
   {"s":"Add the flour and almonds and beat until blended. Cover and refrigerate for 1 hour.","t":60},
   {"s":"Shape 1 tablespoon of dough around each Kiss, covering it completely, and form into a ball."},
   {"s":"Bake at 375°F on an ungreased cookie sheet for 8–12 minutes.","t":12},
   {"s":"Cool completely, then sprinkle powdered sugar over the tops."},
   {"s":"Melt the chocolate chips and shortening in the microwave. Watch closely: if it goes too long it will scorch."},
   {"s":"Drizzle over the tops and let the chocolate harden."}],
 "notes":[]
},
{
 "id":"tawny-pumpkin-pie","title":"Tawny Pumpkin Pie","cat":"Desserts",
 "card":"tawny-pumpkin-pie.jpg","back":"tawny-pumpkin-pie-back.jpg","cook":45,
 "facts":[["Oven","425°F, then 350°F"],["Bake","15 min + 30 min"],["Pie","9-inch"]],
 "groups":[{"items":[
   {"q":1,"i":"unbaked 9-inch pie shell"},
   {"q":1,"u":"can","i":"canned pumpkin (Libby's)","nus":"15 oz","ge":425},
   {"q":0.75,"u":"cup","i":"sugar","gpc":200},
   {"q":0.5,"u":"tsp","i":"salt"},
   {"q":0.25,"u":"tsp","i":"ginger"},
   {"q":1,"u":"tsp","i":"cinnamon"},
   {"q":2,"i":"eggs, slightly beaten"},
   {"q":1,"u":"cup","i":"evaporated milk","n":"\"canned milk\""},
   {"q":0.5,"u":"tsp","i":"vanilla"}]}],
 "steps":[
   {"s":"Combine the pumpkin, sugar, salt and spices in a mixing bowl."},
   {"s":"Add the eggs and mix well."},
   {"s":"Add the milk and vanilla. Mix."},
   {"s":"Pour into the pie shell."},
   {"s":"Bake at 425°F for 15 minutes.","t":15},
   {"s":"Lower the oven to 350°F and bake 30 minutes more, until a knife inserted in the center comes out clean.","t":30}],
 "notes":[]
},
{
 "id":"pumpkin-pecan-pie","title":"Pumpkin Pecan Pie","cat":"Desserts",
 "card":"pumpkin-pecan-pie.jpg","back":"pumpkin-pecan-pie-back.jpg","cook":50,
 "facts":[["Oven","400°F, then broil"],["Pie","9-inch"],["Serves","",8]],
 "groups":[
   {"name":"Pie","items":[
     {"q":1,"i":"uncooked 9-inch pie shell"},
     {"q":2,"i":"eggs, slightly beaten"},
     {"q":2,"u":"cup","i":"pumpkin","nus":"1 lb, 1 small can","gpc":245},
     {"q":0.75,"u":"cup","i":"sugar","gpc":200},
     {"q":0.5,"u":"tsp","i":"salt"},
     {"q":1,"u":"tsp","i":"cinnamon"},
     {"q":0.5,"u":"tsp","i":"ginger"},
     {"q":0.25,"u":"tsp","i":"cloves"},
     {"q":1,"u":"can","i":"evaporated milk","nus":"12 oz","ge":354}]},
   {"name":"Caramelized topping","items":[
     {"q":3,"u":"tbsp","i":"soft butter"},
     {"q":1/3,"u":"cup","i":"brown sugar","gpc":200},
     {"q":1/3,"u":"cup","i":"coarsely chopped pecans","gpc":115}]}],
 "steps":[
   {"s":"Blend the eggs and pumpkin. Stir in the sugar, salt, cinnamon, ginger and cloves. Blend in the milk."},
   {"s":"Pour into the pie shell."},
   {"s":"Bake at 400°F for about 40–50 minutes, until a knife inserted halfway between the edge and the center comes out clean.","t":50},
   {"s":"Cool completely."},
   {"s":"Topping: using a pastry blender, mix the soft butter, brown sugar and pecans."},
   {"s":"Crumble teaspoonfuls of the brown sugar mix over the pie with your fingers (this breaks up the clumps)."},
   {"s":"Broil 5 inches below the heat until bubbly, about 1 minute. Watch closely.","t":1}],
 "tips":["Yummy!"],
 "notes":[]
},
{
 "id":"holiday-turkey","title":"Traditional Holiday Turkey","cat":"Mains",
 "fromline":"From Reynolds",
 "card":"reynolds-oven-bag-recipes.jpg","back":"reynolds-oven-bag-chart.jpg","cook":180,
 "facts":[["Oven","350°F"],["Bake","1½–3 hours, by weight"],["Done","180°F in the thigh"],["Allow","½ lb per person"]],
 "groups":[{"items":[
   {"q":1,"i":"Reynolds Oven Bag, turkey size"},
   {"q":1,"u":"tbsp","i":"flour"},
   {"q":2,"u":"stalk","i":"celery, sliced"},
   {"q":1,"i":"medium onion, sliced"},
   {"q":10,"q2":24,"u":"lb","i":"turkey, completely thawed"},
   {"i":"vegetable oil"}]}],
 "steps":[
   {"s":"Heat the oven to 350°F."},
   {"s":"Shake the flour in the oven bag and place it in a roasting pan at least 2 inches deep. Spray the inside of the bag with nonstick spray to reduce sticking, if desired."},
   {"s":"Add the vegetables to the bag."},
   {"s":"Remove the neck and giblets from the turkey. Rinse and pat dry. Lightly stuff with your favorite stuffing, if desired. Brush the turkey with oil."},
   {"s":"Place the turkey in the bag on top of the vegetables. Close the bag with the nylon tie and cut six ½-inch slits in the top."},
   {"s":"Insert a meat thermometer through the bag into the thickest part of the inner thigh, not touching the bone. Tuck the ends of the bag into the pan."},
   {"s":"Bake until the thermometer reads 180°F: 1½–2 hours for 10–12 lb, 2–2¼ hours for 12–16 lb, 2¼–2½ hours for 16–20 lb, 2½–3 hours for 20–24 lb. Add ½ hour for a stuffed turkey.","t":180},
   {"s":"For easy slicing, let it stand in the bag for 15 minutes. If the turkey sticks to the bag, gently loosen the bag before cutting open the top.","t":15}],
 "tips":["Herb roasted version: instead of plain oil, brush with 2 tbsp vegetable oil or melted butter, then rub with 1 tbsp dried sage, 1 tsp each dried thyme, basil, rosemary, paprika and seasoned salt, and ½ tsp pepper. Spray the bag with nonstick spray if desired (helps with large turkeys).",
          "Two turkey breasts at once: two bone-in breasts (4–8 lb each) with 2 onions cut in eighths and 4 sliced celery stalks, brushed with oil and sprinkled with seasoned salt and pepper. Bake at 350°F for 1½–2 hours, until 170°F; let stand 10 minutes.",
          "Oven-bag chart (on the back): whole stuffed turkey 180°F (stuffing 165°F); bone-in turkey breast 1¾–2¼ hr and boneless 2½–3 hr for 8–12 lb, both to 170°F.",
          "Never set the oven above 400°F with an oven bag, and don't let the bag touch the oven walls or heating elements."],
 "notes":[]
},
{
 "id":"holiday-ham","title":"Traditional Holiday Ham","cat":"Mains",
 "fromline":"From Reynolds",
 "card":"reynolds-oven-bag-recipes.jpg","back":"reynolds-oven-bag-chart.jpg","cook":195,
 "facts":[["Oven","325°F"],["Bake","2½–3¼ hours"],["Done","140°F"],["Allow","½ lb per person"]],
 "groups":[{"items":[
   {"q":1,"i":"Reynolds Oven Bag, turkey size"},
   {"q":1,"u":"tbsp","i":"flour"},
   {"q":12,"q2":16,"u":"lb","i":"fully cooked whole ham, bone-in"},
   {"i":"whole cloves"}]}],
 "steps":[
   {"s":"Heat the oven to 325°F."},
   {"s":"Shake the flour in the oven bag and place it in a roasting pan at least 2 inches deep."},
   {"s":"Trim the skin and fat from the ham, leaving a thin layer of fat. Lightly score the surface in a diamond pattern and insert the cloves."},
   {"s":"Place the ham in the bag. Close with the nylon tie and cut six ½-inch slits in the top."},
   {"s":"Insert a meat thermometer through the bag into the thickest part of the ham, not touching the bone. Tuck the ends of the bag into the pan."},
   {"s":"Bake 2½–3¼ hours, until the thermometer reads 140°F.","t":195},
   {"s":"Let it stand in the bag for 15 minutes before slicing.","t":15}],
 "tips":["Oven-bag chart (on the back): half bone-in ham (8–10 lb) 2–2½ hr; boneless half ham (10–12 lb) 2¼–2¾ hr with ½ cup water; spiral-sliced ham (8–10 lb) 1½–1¾ hr, cut side down — all to 140°F."],
 "notes":[]
},
]

# Recipes waiting on missing info.
# Pizza: Ali is checking whether there's a second "Pizza Crust ②" card. Card photos are in cards/on-hold/
# (pizza-crust-card1 + back, pizza-card2 + back). Agreed: one "Pizza" recipe; 1 tbsp olive oil total on the crusts.
# Mystery cake (batch 7): only the back of the card (9x13 cake, 350°F, brown-sugar glaze topping with nuts) —
# photo in cards/on-hold/mystery-cake-back.jpg. Waiting for the matching front card.
# Batch 8 holds (photos in cards/on-hold/):
# Mandarin Orange Cake (Lois Dotson; card says "(over)" — need the back: nuts, pan, temp, time);
# Marinated Mushrooms (front + back complete, but the back says "over…" — waiting for a possible 3rd side; goes in Appetizers);
# Oysters Rockefeller Spread (same cookbook page as Layered Seafood Spread; method on the next page; Appetizers).
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

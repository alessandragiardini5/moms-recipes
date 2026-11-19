"""Mom's recipes — the only file to edit when adding or correcting recipes.

Recipe fields: id, title, cat, card (photo in cards/), back (optional photo of the card's back),
from (default "Mom"; "Angela" for cards signed A. Dotson), cook (minutes, for HomeView),
facts, groups, steps, tips (Mom's tips shown as "Mom's tips"), notes (open questions only).

Ingredient fields:
  q    amount as a number (1.5, 4/3, 0.25) — leave out when the card gives none
  q2   upper end of a range ("¾–1 cup" -> q 0.75, q2 1)
  pre  word before the amount, e.g. "about"
  u    unit, singular: cup, tbsp, tsp, oz, lb, can, cube, package, loaf, handful, bunch, strip,
       square, bag, small bottle (none for "3 eggs")
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
]

# Recipes waiting on missing info (none right now)
ON_HOLD = []

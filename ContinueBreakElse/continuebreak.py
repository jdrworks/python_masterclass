# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         continue;
#     print("buy " + item)
meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = False
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that then please")
if nasty_food_item:
    print("Can't I have anything without spam in it")
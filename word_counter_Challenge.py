input_str = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

de_1 = ""


for i in input_str:
    if i.isalnum() or i.isspace() and i == "-":
        de_1 += i
        print(de_1)


words = de_1.split()
num_words = len(words)
print(words)
print(num_words)

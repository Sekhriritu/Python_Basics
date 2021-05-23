val_dict = {1: "a", 2: "b", 3: "c", 4: 45.6, 5: False}
print(val_dict[3])

print(5 in val_dict)
print(10 not in val_dict)

# methods exercise-1

print("methods exercise-1")

test = {"Queen": "Bohemian Rhapsody",
        "Bee Gees": "Stayin' Alive",
        "U2": "One",
        "Michael Jackson": "Billie Jean",
        "The Beatles": "Hey Jude",
        "Bob Dylan": "Like A Rolling Stone"}

print(len(test))

for key in test.keys():
    print(key)

print(test.values())


for key, value in test.items():
    print(key, value)


print(test.get("Promise of the Real", "value not found"))


# methods exercise-2

print("methods exercise-2")


test_1 = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")

for key1, value1 in test_1.items():
    print(key1, value1)

fast_food_items = {"McDonald's": "Big Mac",
                   "Burger King": "Whopper",
                   "Chick-fil-A": "Original Chicken Sandwich"}

var_val = fast_food_items.pop("McDonald's")
print(var_val)

print(fast_food_items.popitem())

# methods exercise-3

print("methods exercise-3")

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)
print(internet_celebrities)

celebs = internet_celebrities.copy()
print(celebs)

internet_celebrities.clear()
print(internet_celebrities)




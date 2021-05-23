# loops for tuples

# for loop

major_cities = ("Sydney", "New York", "London", "Paris", "Tokyo")

for city in major_cities:
    print(city)


# While loop

count = 0
while count < len(major_cities):
    print(major_cities[count])
    count += 1


# While loop backwards

backwards = len(major_cities)-1

while backwards >= 0:
    print(major_cities[backwards])
    backwards -=1



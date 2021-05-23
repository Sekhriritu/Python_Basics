var = range(1, 50)


for num in var:
    if num % 5 == 0 & num % 3 == 0:
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)





# Exercise functions with no params

def hello_world_printer():
    print("hello world!")


hello_world_printer()


# Exercise functions with one params


def name_printer(name):
    print(name)


name = input("enter your name")
name_printer(name)


# Volume of the Rectangular Prism

def vol_prism(length, width, height):
    return length * width * height


length = int(input("Enter the length"))
width = int(input("Enter the width"))
height = int(input("Enter the height"))

print("The volume of the rectangular prism is " + str(vol_prism(length, width, height)) + " cubic feet.")

# Programming Challenge: Celsius to Fahrenheit

temp_celsius = int(input("Enter the temperature"))


def func_fahrenheit(temp_celsius):
    return round(1.8 * temp_celsius + 32, 1)


print("Temp in Fahrenheit is " + str(func_fahrenheit(temp_celsius)))


def func_fahrenheit1(temp_celsius):
    return ((18 * temp_celsius + 320)/10)


print("Temp in Fahrenheit is " + str(func_fahrenheit1(temp_celsius)))




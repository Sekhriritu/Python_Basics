

def factorial(var_int):
    ret = 1
    for num in range(var_int, 1, -1):
        ret *= num
    return ret


print(factorial(3))
print(factorial(4))
print(factorial(5))






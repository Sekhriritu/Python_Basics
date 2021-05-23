user_str = input("Enter a string.")
long_Str = len(user_str)

emp_string = ""

for str_val in range(long_Str-1, -1, -1):
    emp_string += user_str[str_val]


print(emp_string)
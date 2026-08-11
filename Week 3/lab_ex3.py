code_one = input("Enter Code 1: ")
code_two = input("Enter Code 2: ")
code_three = input("Enter Code 3: ")
tuple_codes_self = (code_one, code_two, code_three)

code_one = input("Enter Code 1: ")
code_two = input("Enter Code 2: ")
code_three = input("Enter Code 3: ")
tuple_codes_super = (code_one, code_two, code_three)

tuple_unique_codes = tuple(set(tuple_codes_self) | set(tuple_codes_super))

print(tuple_unique_codes)
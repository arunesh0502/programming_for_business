list_codes_self = []

for count in range(0, 3):
    code = input("Enter Code: ")
    list_codes_self.append(code)

tuple_codes_self = tuple(list_codes_self)


list_codes_super = []

for count in range(0, 3):
    code = input("Enter Code: ")
    list_codes_super.append(code)

tuple_codes_super = tuple(list_codes_super)


tuple_unique_codes = tuple(
    set(tuple_codes_self).union(set(tuple_codes_super))
)

print(tuple_unique_codes)
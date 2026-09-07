input_list = ["IVV", "ATEC", "SQ2", "RIO", "VDHG", "A200"]

four_list = list(filter(lambda x: len(x) == 4, input_list))

three_list = list(filter(lambda x: len(x) == 3, input_list))

print(four_list)
print(three_list)
number_of_sales = int(input("Enter number of sales: "))

sale_list = []

for sale in range(number_of_sales):
    sale_value = float(input("Enter sale value: "))
    sale_list.append(sale_value)

free_list = list(map(lambda value: value / 1.1, sale_list))

print(free_list)
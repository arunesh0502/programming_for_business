sale_one = float(input("Enter Sale 1: "))
sale_two = float(input("Enter Sale 2: "))
sale_three = float(input("Enter Sale 3: "))
sale_four = float(input("Enter Sale 4: "))
sale_list = [sale_one, sale_two, sale_three, sale_four]

# Multiply and Divide
sale_list[1] *= 1.1
sale_list[3] *= 1.1
sale_list[0] /= 1.1
sale_list[2] /= 1.1

sale_five = float(input("Enter Sale 5: "))
sale_list.insert(1, sale_five)

grand_total = sum(sale_list)
print(grand_total)

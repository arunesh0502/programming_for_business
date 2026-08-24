sale_list = []

for sale_number in range(1, 6):

    sale = float(input("Enter Sale " + str(sale_number) + ": "))

    while sale <= 0:
        print("Sale must be a positive value.")
        sale = float(input("Enter Sale " + str(sale_number) + ": "))

    sale_list.append(sale)


for sale_number in range(0, 5):

    if sale_number == 1 or sale_number == 3:
        sale_list[sale_number] = sale_list[sale_number] * 1.1
    else:
        sale_list[sale_number] = sale_list[sale_number] / 1.1


grand_total = 0

for sale_number in range(0, 5):
    grand_total = grand_total + sale_list[sale_number]

print(grand_total)

#--------------------------------------------------
# Without WHILE Loop, positive checker and merging
#--------------------------------------------------

sale_list = []

for count in range(1, 6):

    sale = float(input("Enter Sale " + str(count) + ": "))

    sale_list.append(sale)


for count in range(0, 5):

    if count % 2 == 1:
        sale_list[count] = sale_list[count] * 1.1
    else:
        sale_list[count] = sale_list[count] / 1.1


grand_total = 0

for count in range(0, 5):

    grand_total = grand_total + sale_list[count]

print(grand_total)
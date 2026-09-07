sale_one = float(input("Enter Sale 1: "))
sale_one_treatment = input(
    "Enter GST Treatment for Sale 1 (GST-inclusive or GST-exclusive): "
)
if sale_one_treatment == "GST-inclusive":
    sale_one_adjusted = sale_one
else:
    sale_one_adjusted = sale_one * 1.1

sale_two = float(input("Enter Sale 2: "))
sale_two_treatment = input(
    "Enter GST Treatment for Sale 2 (GST-inclusive or GST-exclusive): "
)
if sale_two_treatment == "GST-inclusive":
    sale_two_adjusted = sale_two
else:
    sale_two_adjusted = sale_two * 1.1

sale_three = float(input("Enter Sale 3: "))
sale_three_treatment = input(
    "Enter GST Treatment for Sale 3 (GST-inclusive or GST-exclusive): "
)
if sale_three_treatment == "GST-inclusive":
    sale_three_adjusted = sale_three
else:
    sale_three_adjusted = sale_three * 1.1

sale_four = float(input("Enter Sale 4: "))
sale_four_treatment = input(
    "Enter GST Treatment for Sale 4 (GST-inclusive or GST-exclusive): "
)
if sale_four_treatment == "GST-inclusive":
    sale_four_adjusted = sale_four
else:
    sale_four_adjusted = sale_four * 1.1

sale_list = [sale_one_adjusted, sale_two_adjusted, sale_three_adjusted, sale_four_adjusted]

sale_five = float(input("Enter Sale 5: "))
sale_five_treatment = input(
    "Enter GST Treatment for Sale 5 (GST-inclusive or GST-exclusive): "
)
if sale_five_treatment == "GST-inclusive":
    sale_five_adjusted = sale_five
else:
    sale_five_adjusted = sale_five * 1.1

sale_list.insert(1, sale_five_adjusted)
grand_total = round(sale_list[0] + sale_list[1] + sale_list[2] + sale_list[3] + sale_list[4], 2)
print("Grand Total (GST Applied): ", grand_total)
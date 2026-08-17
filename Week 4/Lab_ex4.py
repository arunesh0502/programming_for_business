airfare = float(input("Enter the airfare per ticket: "))
number_of_tickets = int(input("Enter the number of tickets: "))
ticket_type = input("Enter ticket type (Economy, Business or First): ")

if ticket_type == "Economy":
    tax_rate = 0.02
elif ticket_type == "Business":
    tax_rate = 0.03
elif ticket_type == "First":
    tax_rate = 0.04
else:
    print("Please try again")

total_airfare = airfare * number_of_tickets
total_tax = total_airfare * tax_rate

print(total_tax)
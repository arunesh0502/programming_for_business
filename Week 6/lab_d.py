def tax_calculator(*args):
    tax_payable = 0

    if len(args) < 1:
        print("Error: At least one ticket is required.")
    else:
        for ticket in args:
            ticket_price = ticket[0]
            ticket_type = ticket[1]

            if ticket_type == "E":
                tax_rate = 0.02
            elif ticket_type == "B":
                tax_rate = 0.03
            elif ticket_type == "F":
                tax_rate = 0.04

            ticket_tax = ticket_price * tax_rate
            tax_payable = tax_payable + ticket_tax

    return tax_payable


print(tax_calculator((100, "E"), (1000, "B")))
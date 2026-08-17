currency_value = float(input("Enter the currency value: "))
conversion = input("Enter currency to convert to (USD or AUD): ")

if conversion == "AUD":
    result = currency_value * 1.54
    print(result)
else:
    result = currency_value / 1.54
    print(result)
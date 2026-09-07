def currency_converter(currency_value, to_aud):
    converted_value = 0

    if to_aud == True:
        converted_value = currency_value * 1.54
    elif to_aud == False:
        converted_value = currency_value / 1.54

    return converted_value


print(currency_converter(66, True))
print(currency_converter(100, False))
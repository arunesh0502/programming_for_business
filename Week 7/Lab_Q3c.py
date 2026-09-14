import math

base_value = int(input("Enter a number: "))

for power in range(0, 6):
    result = math.pow(base_value, power)
    print(str(base_value) + "^" + str(power) + "=" + str(result))
length = float(input("Enter the length of the shipment: "))
width = float(input("Enter the width of the shipment: "))
height = float(input("Enter the height of the shipment: "))

volume = length * width * height

if volume < 10:
    print("Standard truck is required.")
elif volume >= 10 and volume <= 20:
    print("B-Double truck is required.")
elif volume > 20 and volume < 30:
    print("B-Triple truck is required.")
else:
    print("Please try again.")
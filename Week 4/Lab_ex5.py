length = float(input("Enter the length of the shipment: "))
width = float(input("Enter the width of the shipment: "))
height = float(input("Enter the height of the shipment: "))

volume = length * width * height

if volume < 10:
    print("A standard truck is required.")
elif volume >= 10 and volume <= 20:
    print("A B-Double truck is required.")
elif volume > 20 and volume < 30:
    print("A B-Triple truck is required.")
else:
    print("Please re-calculate your shipment and try again.")
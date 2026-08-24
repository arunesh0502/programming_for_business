dimensions = []

for count in range(0, 3):

    dimension = float(input("Enter the dimension: "))

    dimensions.append(dimension)


length = dimensions[0]
width = dimensions[1]
height = dimensions[2]

volume = length * width * height

if volume < 10:
    print("Standard truck is required.")

elif volume >= 10 and volume <= 20:
    print("B-Double truck is required.")

elif volume > 20 and volume < 30:
    print("B-Triple truck is required.")

else:
    print("Please try again.")
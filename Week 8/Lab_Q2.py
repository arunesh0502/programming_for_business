import numpy as np

data_list = list(range(0, 24, 2))

numpy_array = np.array(data_list)
print("Original Array:")
print(numpy_array)

four_by_three_array = np.reshape(numpy_array, (4, 3))
print("4x3 Array:")
print(four_by_three_array)

three_by_four_array = np.reshape(numpy_array, (3, 4))
print("3x4 Array:")
print(three_by_four_array)

divided_array = np.divide(numpy_array, 2)
print("After division by 2:")
print(divided_array)

import os

path = input("Enter a directory path: ")
directory_list = os.listdir(path)

for each_file in directory_list:
    print(each_file)
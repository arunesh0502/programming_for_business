import random


def bingo_function(number_list, selected_number):
    random_number = random.choice(number_list)

    if random_number == selected_number:
        print("Bingo")
    else:
        print("Try again")

bingo_function([10, 20, 30, 40, 50], 30)
# day_44_100_days_bingoGame

# remember list[row_index][column_index]

from random import randint
import os
import time


def create_bingo_card():
    """This function creates a bingo card with eight random numbers and the word 'BINGO' in the center."""
    # random integers between 0-90
    # use a list comprehension to get a list of numbers
    # convert it to a set for unique nums

    nums_set = set()
    while len(nums_set) < 8:
        nums_set.add(randint(0, 90))

    nums_list = list(nums_set)
    nums_list.sort()

    # assign numbers to bingo card
    bingo_card = [
        [nums_list[0], nums_list[1], nums_list[2]],
        [nums_list[3], "BINGO", nums_list[4]],
        [nums_list[5], nums_list[6], nums_list[7]],
    ]

    return bingo_card


def pretty_print(card):
    """This function takes in the bingo card and prints it out in am easy to view manner."""
    print()
    for row in card:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()


def get_valid_input():
    """This function ensures the user enters a valid integer between 0 and 90"""
    while True:
        try:
            # ask the user what number is next
            user_input = int(input("What number is next on the bingo card? "))

            if 0 <= user_input <= 90:
                return user_input
            else:
                print("Please enter a number between 0 and 90.")
        except ValueError:
            print("Invalid input. Please enter an integer")


# initialize game
my_card = create_bingo_card()


count_x = 0
# list to store guessed numbers
guessed_numbers = set()

while count_x < 8:
    pretty_print(my_card)
    # get valid input from user
    user_input = get_valid_input()

    if user_input in guessed_numbers:
        print(f"You have already guessed {user_input}. Try again.")
        continue

    # look for number in bingo card
    found = False
    for row in my_card:
        for i, item in enumerate(row):
            # check if input is in the bingo card
            if user_input == item:
                # reassign the value to 'X'
                # or my_card[row][item] = 'X'
                row[i] = "X"
                # increment 'count_x' by one
                count_x += 1
                guessed_numbers.add(user_input)
                found = True
                break
        if found:
            break
    if not found:
        print(f"{user_input} is not on the Bingo card.")
    time.sleep(1)
    os.system("clear")

print(f"You won! You guessed all {count_x} numbers.")

# day_21_of_100_days_mathGame

from random import randint
import os # systme.clear
import time # time.sleep(5)

# prompt the user for a multiplication table
try:
    user_number = int(
        input("Enter a number to do the multiplication table from 1-10: ")
    )
except ValueError:
    print("Please enter a valid integer.")
    exit()

user_points = 0

# generate a list of random integers from zero to ten
rand_ints_list = [randint(0, 10) for x in range(0, 10)]

# generate multiplication table from one to ten time the user's number
# ask them as questions, as in 'what is 1 x 7 = ? '
for number in rand_ints_list:
    answer = number * user_number

    # input validation
    try:
        user_answer = int(input(f"What is {number} x {user_number}? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    # if user gets the answer correct they get one point
    if user_answer == answer:
        user_points += 1
        if user_points == 10:
            print("Congrats!")

    # if wrong answer, user gets no points and told what correct answer is
    else:
        print(f"Incorrect, the correct answer is {answer}.")

print(f"Final score, you have {user_points} points.")

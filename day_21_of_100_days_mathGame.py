# day_21_of_100_days_mathGame

# prompt the user for a multiplication table
user_number = int(input("Enter a number to do the multiplication table from 1-10: "))
user_points = 0

# generate multiplication table from one to ten time the user's number
# ask them as questions, as in 'what is 1 x 7 = ? '
for number in range(1, 11):
    answer = number * user_number

    user_answer = int(input(f"What is {number} x {user_number}? "))

    # if user gets the answer correct they get one point
    if user_answer == answer:
        user_points += 1
        if user_points == 10:
            print('Congrats!')

    # if wrong answer, user gets no points and told what correct answer is
    else:
        print(f"Incorrect, the correct answer is {answer}.")

print(f'Final score, you have {user_points} points.')

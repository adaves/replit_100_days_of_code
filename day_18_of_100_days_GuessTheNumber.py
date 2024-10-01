# day_18_of_100_days_GuessTheNumber
# pick a random number for user to guess, between zero and one million
from random import randint

# random will pick the target variable
target = randint(0, 1000000)
print(f"Target variable: {target}")
# variable to keep track of the amount of user guesses
user_guess_count = 0


# define a function to take an int paramter, to return the binary search guess count
def binary_search_guess_count(low, high, target):
    guesses = 0
    while low <= high:
        guesses += 1
        mid = (low + high) // 2
        if mid == target:
            return guesses
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return guesses


guesses_remaining = binary_search_guess_count(0, 1_000_000, target) - user_guess_count

# use a while loop to keep asking user to guess number
while True:
    print(f"{guesses_remaining} guesses available.")
    user_guess = int(input("Guess an integer from zero to one million: "))
    # keep track of guess count
    user_guess_count += 1
    guesses_remaining = (
        binary_search_guess_count(0, 1_000_000, target) - user_guess_count
    )
    # if user picks the number, user wins
    if user_guess == target:
        print(
            f"Correct, you win!\nUser guess count: {user_guess_count}\nGuesses remaining: {guesses_remaining}"
        )
        break
    # if a negative number is chosen, progam will exit
    elif user_guess < 0:
        print(
            f"Wrong!\nUser guess count: {user_guess_count}\nGuesses remaining: {guesses_remaining}"
        )
        exit()
    # if user guess is too high, inform user guess is too high
    elif user_guess > target:
        print(
            f"Too high, guess again.\nUser guess count: {user_guess_count}\nGuesses remaining: {guesses_remaining}"
        )
        continue
    # if user guess is too low, inform user guess is too low
    elif user_guess < target:
        print(
            f"Too low, guess again.\nUser guess count: {user_guess_count}\nGuesses remaining: {guesses_remaining}"
        )
        continue
    else:
        print("Error")
        exit()

# day_39_100_days_hangman_game
import random

# make a list of ten words
words = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
]

# pick a random word from the list of words
word_to_guess = random.choice(words)
alphabet = set("abcdefghijklmnopqrstuvwxyz")
blank_word_to_guess = list(
    "_" if letter in alphabet else letter for letter in word_to_guess
)
# [letter.replace(letter, '_') for letter in blank_word_to_guess if letter in alphabet]

# list to store the letters the user has guessed
letters_user_has_guessed = []


def difficulty_level(word):
    easy = 2 * len(word)
    medium = 2 + len(word)
    hard = len(word)

    user_input = (
        input(
            'Pick a difficulty level, easy, medium, or hard. Enter "e", "m", or "h": '
        )
        .strip()
        .lower()
    )
    if user_input == "e":
        return easy
    elif user_input == "m":
        return medium
    elif user_input == "h":
        return hard
    else:
        print("Error")


while True:
    # pick a difficulty level
    user_difficulty_level = difficulty_level(word_to_guess)

    while user_difficulty_level > 0:
        # show user how many guesses they have left
        print(f"You have {user_difficulty_level} guesses left")
        print()

        # show user the word to guess
        print(f'Your word to guess: {"".join(blank_word_to_guess)}')
        print()

        # prompt the user to type in a letter
        user_input = input("Enter a letter: ").strip().lower()

        # add guessed word to list to keep track
        if user_input not in letters_user_has_guessed:
            letters_user_has_guessed.append(user_input)

            # check is user_input is in word_to_guess
            if user_input in word_to_guess:
                print(f"{user_input} is in the word to guess")
                print()

                # insert their picked letter, '_a_'
                # if user_input is in word_to_guess, replace the blank with the letter

                for index, letter in enumerate(word_to_guess):
                    if letter == user_input:
                        blank_word_to_guess[index] = user_input
                print(f'Your word to guess: {"".join(blank_word_to_guess)}')
                print()

            else:
                print(f"{user_input} is not in the word to guess")
                print()

            # decrement the user_difficulty_level
            user_difficulty_level -= 1

            if "_" not in blank_word_to_guess:
                print("You win!")
                break
        else:
            print("You have already guessed that letter.")

    if "_" not in blank_word_to_guess or user_difficulty_level == 0:
        break
if "_" in blank_word_to_guess:
    print("You lose!")

# day_48_100_days

import os, time

while True:
    f = open(
        r"C:\Users\adame\OneDrive\Desktop\python_scripts\replit_100_days_of_code\day48_100days.txt",
        "a+",
    )
    try:
        user_input = input("Enter initials like (AED) followed by your high score: ").upper()
        user_input = user_input.split(" ")
        initials, high_score = user_input

        f.write(f'{initials} {high_score}\n')
    except ValueError:
        os.system('cls')
        print('Enter initials followed by a space and then your high score.')
        time.sleep(3)
        os.system('cls')

    

    f.close()

    time.sleep(1)
    os.system("cls")

    end = input("Are you finished? y/n: ")
    if end == "y":
        break
    else:
        continue

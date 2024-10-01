# day_20_of_100_days_rangeFunction

user_start = int(input("Enter a number to start at: "))
user_end = int(input("Enter a number to end at: "))
user_increment = int(input("Enter a number to count by: "))

for number in range(user_start, user_end, user_increment):
    print(number)

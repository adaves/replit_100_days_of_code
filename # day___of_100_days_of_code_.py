# day___of_100_days_of_code_

my_list = []

while True:
    list_action = input('What action do you want to take, add or remove? ')

    if list_action.strip().lower() == 'add':
        add = input('What do you want to add to the list? ')
        my_list.append(add)

    elif list_action.strip().lower() == 'remove':
        remove = input('What do you want to remove from the list? ')
        my_list.remove(remove)

    print(my_list)
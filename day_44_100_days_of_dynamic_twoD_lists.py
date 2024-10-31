# day_44_100_days_of_dynamic_twoD_lists.py

list_of_shame = []


def pretty_print():
    print()
    for row in list_of_shame:
        for item in row:
            print(f"{item:^10}", end=" | ")
        print()
    print()


while True:
    menu = input("Add or Remove? ").strip().lower()
    if menu[0] == "a":
        name = input("Enter name: ")
        age = input("Enter age: ")
        pref = input("Enter computer platform: ")
        row = [name, age, pref]
        list_of_shame.append(row)
    else:
        name = input("What is the name of the record you want to delete? ")
        for row in list_of_shame:
            if name in row:
                # fix this line
                list_of_shame.remove(row)

    pretty_print()
    """exit = input('Exit y/n? ').strip().lower()
    if (exit[0] == 'y'):
        break"""

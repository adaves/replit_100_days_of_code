# day_45_100_days_of_code_toDo_list_manager.py

import os, time

# to do list for the script
to_do_list = {}
# counter for dynamic key naming
counter = 1


# make a menu that can --> add, view, remove, edit
def menu():
    output = (
        input(
            """\nThis is your To Do List manager, please pick an option.\n\n1. Add, to add an item. Enter '1'\n2. View, to view the entire list or view items by priority. Enter '2'\n3. Edit, to change an item in the To Do List. Enter '3'\n4. Remove, to remove an item from the list entirely. Enter '4'\n """
        )
        .strip()
        .lower()
    )
    return output


# add --> what to add, when its due (the day of the week and date), priority level high, med, or low
def add(to_do_list, counter):
    time.sleep(1)
    os.system("clear")
    item = input("What would you like to add? ").strip().lower()
    due_date = input("When is this item due by? ").strip().lower()
    priority = input("What priority level, high, medium, or low? ").strip().lower()

    new_item = {
        f"item_{counter}": {"item": item, "due_date": due_date, "priority": priority}
    }
    # update to do list with new item
    to_do_list.update((new_item))
    counter += 1

    return to_do_list, counter


# view --> view all using pretty print, view by priority
def view():
    """This function allows the user to view the entire list or view entries by priority level"""

    time.sleep(1)
    os.system("clear")

    user_input = (
        input(
            'What would you like to view, the entire list or items by priority? Enter "a" or "p": '
        )
        .strip()
        .lower()
    )
    print()

    while True:
        # take user input and decide what to do
        if user_input == "a":
            for item, dict in to_do_list.items():
                for key, value in dict.items():
                    print(f"{key} : {value}")
                print()
            break

        elif user_input == "p":
            priority = (
                input(
                    'What priority level would you like to see, "High", "Medium", or "Low"? Enter "h", "m", or "l": '
                )
                .strip()
                .lower()
            )
            if priority == "h":
                for key, value in to_do_list.items():
                    if value["priority"] == "high":
                        print(value)
                break

            elif priority == "m":
                for key, value in to_do_list.items():
                    if value["priority"] == "medium":
                        print(value)
                break

            elif priority == "l":
                for key, value in to_do_list.items():
                    if value["priority"] == "low":
                        print(value)
                break

            else:
                print(
                    f'Error, invalid input. You entered {priority},please enter either "h", "m", or "l".'
                )
                continue

        else:
            print(f"Error, invalid input. You entered {user_input}. ")

        time.sleep(1)
        os.system("clear")


# edit --> change any info in one of the to-dos


def edit(to_do_list, counter):
    """docstring"""

    time.sleep(1)
    os.system("clear")

    user_input = input("What item would you like to edit? ")

    for key in list(to_do_list.keys()):
        if user_input in to_do_list[key]["item"]:
            to_edit = input(
                'What would you like to edit, the item, the due date, or the priority? Enter "item", "due_date", "priority", or "all". '
            )
            if to_edit == "item":
                item = input("Enter the new item? ").strip().lower()
                to_do_list[key]["item"] = item
                break

            elif to_edit == "due_date":
                due_date = input("What is the new due date? ").strip().lower()
                to_do_list[key]["due_date"] = due_date
                break

            elif to_edit == "priority":
                priority = input("Enter the new priority level. ").strip().lower()
                to_do_list[key]["priority"] = priority
                break

            elif to_edit == "all":
                item = input("Enter the new item? ").strip().lower()
                due_date = input("What is the new due date? ").strip().lower()
                priority = input("Enter the new priority level. ").strip().lower()

                to_do_list[key]["item"] = item
                to_do_list[key]["due_date"] = due_date
                to_do_list[key]["priority"] = priority
                break
            else:
                print(f"Incorrect option, you entered {to_edit}.")

        else:
            print(
                f"The item you wanted to Edit, {user_input} is not in the To Do List."
            )


# remove --> completely remove
def remove():
    # get the item the user wants to remove
    item = input("What item would you like to remove? ").strip().lower()

    # Iterate over a copy of the keys to avoid modifying the dictionary during iteration
    for key in list(to_do_list.keys()):
        if item in to_do_list[key]["item"]:
            del to_do_list[key]
            print(f"The item you wanted to remove, {item} has been removed.")
        else:
            print()


# put it into action
while True:
    # call the menu function to get user input
    user_input = menu()

    # use user input to decide what happens next
    if user_input == "1":
        add(to_do_list, counter)

    elif user_input == "2":
        view()

    elif user_input == "3":
        edit(to_do_list, counter)

    elif user_input == "4":
        remove()

    else:
        print(f"Error, incorrect option. You typed {user_input}. Please try again")
        continue

    time.sleep(1)
    os.system("clear")

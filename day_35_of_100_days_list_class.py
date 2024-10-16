class To_do_list:
    import os, time

    def __init__(self):
        self.user_list = []

    def menu(self):
        while True:
            get_input = (
                input(
                    "What would you like to do with your list?\n"
                    "1. Add an item, enter 1: \n"
                    "2. Remove an item, enter 2: \n"
                    "3. View the list, enter 3: \n"
                    "4. Edit an item in the list, enter 4: \n"
                    "5. Clear the list, enter 5:  \n"
                    "To exit, enter exit: "
                )
                .strip()
                .lower()
            )

            if get_input == "1":
                item = input("Enter the item to add: ").strip().lower()
                self.add(item)
            elif get_input == "2":
                item = input("Enter the item to remove: ").strip().lower()
                self.remove(item)
            elif get_input == "3":
                self.view()
            elif get_input == "4":
                self.edit()
            elif get_input == "5":
                self.clear()
            elif get_input == "exit":
                break
            else:
                print("Invalid input, try again.")

    def add(self, item):
        if item not in self.user_list:
            self.user_list.append(item)
        else:
            print("Item is already in the list, cannot add duplicates.")

    def remove(self, item):
        if item in self.user_list:
            self.user_list.remove(item)
        else:
            print("Item not found in list.")

    def view(self):
        if not self.user_list:
            print("The list is empty")
        else:
            print("Current List:")
            for items in self.user_list:
                print(f"- {items}")
            print()

    def edit(self):
        item = input("What list item would you like to edit? ").strip().lower()
        if item in self.user_list:
            index = self.user_list.index(item)
            new_item = input("Enter the new list item.").strip().lower()
            if new_item not in self.user_list:
                self.user_list[index] = new_item
            else:
                print("The new item already exists in the list. Edit not made")
        else:
            print("Item is not in the user list. ")

    def clear(self):
        check_to_clear = (
            input('Are you sure you want to clear the entire list? Enter "y" or "n": ')
            .strip()
            .lower()
        )
        if check_to_clear == "y":
            self.user_list.clear()
        else:
            print("List not cleared")


# test code under here

to_do = To_do_list()
to_do.menu()

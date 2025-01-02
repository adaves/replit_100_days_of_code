# day_50_100_days_idea_storage_system
import random
import os
import time


def menu() -> str:
    """
    Display the menu to the user and get their choice.

    Returns:
    str: User's menu choice.
    """
    print("Menu:")
    print("a. Add an idea")
    print("r. Display a random idea")
    choice = input("Enter your choice: ").strip().lower()
    return choice


def get_idea() -> str:
    """
    Get an idea from the user.

    Returns:
    str: User's idea.
    """
    idea = input("Enter your idea: ").strip()
    return idea


def add(idea: str) -> str:
    """
    Save idea to a text file named my.ideas, append to file.

    Parameters:
    idea (str): The idea to be saved.

    Returns:
    str: Confirmation message.
    """
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(scriptdir, "my.ideas.txt")

    f = open(filepath, "a+")
    f.write(f"{idea}\n")
    f.close()

    return "File saved successfully"


def load() -> list[str]:
    """
    Load all ideas into a list, and split them to make it easier for a random idea to be chosen.

    Returns:
    list[str]: List of ideas.
    """

    scriptdir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(scriptdir, "my.ideas.txt")

    f = open(filepath, "r")
    contents = f.read().split("\n")
    f.close()

    return contents


def display_random_idea() -> str:
    """
    Choose one idea at random to display to the user.

    Returns:
    str: Random idea.
    """
    ideas_list = load()
    output = random.choice(ideas_list)

    return output


if __name__ == "__main__":
    user_menu_choice = menu()

    if user_menu_choice == "a":
        idea = get_idea()
        add(idea)
    elif user_menu_choice == "r":
        rando_idea = display_random_idea()
        print(rando_idea)
    else:
        print(
            "Invalid choice. Please select 'a' to add an idea or 'r' to display a random idea."
        )

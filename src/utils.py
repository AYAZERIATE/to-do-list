import os
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def print_header():
    print("=" * 40)
    print("        TODO LIST APP")
    print("=" * 40)


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M")
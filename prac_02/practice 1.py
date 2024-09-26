import random

def get_valid_name():
    """Prompt the user for a valid (non-empty) name."""

    name = input("Enter your name: ")
    if name:
        return name
    print("Name cannot be empty. Please try again.")

def print_asterisks():
    """Print a line (of asterisks)."""
    print("*" * 30)

def print_random_number():
    """Print a random number between 1 and 100."""
    number = random.randint(1, 100)
    print(f"Random number: {number}")

def main():
    """Main function to run the program."""
    print("Welcome to the program!")
    name = get_valid_name()

    while True:
        print("\nMain Menu:")
        print("1. Get valid (non-empty) name")
        print("2. Print a line (of asterisks)")
        print("3. Print random number")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f"Your name is: {name}")
        elif choice == '2':
            print_asterisks()
        elif choice == '3':
            print_random_number()
        elif choice == '4':
            print(f"Farewell, {name}!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
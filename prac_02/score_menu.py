# score_menu.py

def main():
    score = get_valid_score()

    # Menu loop
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"Your result is: {determine_result(score)}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

# Function to get a valid score (0-100)
def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Function to determine the result based on score
def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

# Function to show stars based on the score
def show_stars(score):
    print("*" * score)

# Call the main function to run the program
if __name__ == "__main__":
    main()

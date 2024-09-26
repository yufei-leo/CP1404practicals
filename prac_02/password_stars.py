def main():
    # Set the minimum password length
    MIN_LENGTH = 8

    # Continuously ask the user for a valid password
    password = input(f"Enter a password (minimum {MIN_LENGTH} characters): ")
    while len(password) < MIN_LENGTH:
        print(f"Error: Password must be at least {MIN_LENGTH} characters long.")
        password = input(f"Enter a password (minimum {MIN_LENGTH} characters): ")

    # Print asterisks based on the length of the password
    print('*' * len(password))

# Call the main function to run the program
if __name__ == "__main__":
    main()

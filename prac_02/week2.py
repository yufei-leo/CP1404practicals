while True:
    try:
        low = int(input("Enter a low number: "))
        high = int(input("Enter a high number: "))
        if high >= low:
            break
        else:
            print("High number must be greater than low number. Please try again.")
    except ValueError:
        print("Please enter an integer.")



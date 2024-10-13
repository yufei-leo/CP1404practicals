# names = ["Ada", "Alan", "Bill", "John"]
# print("Current names:", ", ".join(names))
#
# name_to_remove = input("Who do you want to remove? (Press Enter to stop) ")
#
# while name_to_remove != "":
#     if name_to_remove in names:
#         names.remove(name_to_remove)
#         print("Updated names:", ", ".join(names))
#     else:
#         print(f"{name_to_remove} is not in the list. Please try again.")
#
#     name_to_remove = input("Who do you want to remove? (Press Enter to stop) ")
#
# print("Final list of names:", ", ".join(names))
#
# value = [[3,4,5,1], [33,6,1,2]]
#
# v = value[0][0]
# for row in range(0, len(value)):
#     for column in range(0, len(value[row])):
#         if v < value[row][column]:
#             v = value[row][column]
#
# print(v)

# def main():
#     numbers = get_numbers()
#     squared_numbers = square_numbers(numbers)
#     display_numbers(squared_numbers)
#
# def get_numbers():
#     user_input = input("Enter a number: ")
#     return [float(num) for num in user_input.split(",")]
#
# def squared_numbers(numbers):
#     return [float(num) ** 2 for num in numbers]
#
# def display_numbers(numbers):
#     print('..'. join(map(str, numbers)))
#
# if __name__ == '__main__':
#     main()

data = [['Derek', 71, ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]]

# Loop through each item in the data
for item in data:
    # Print the first element (name) and the second element (score) of the main list
    print(f"{item[0]} {item[1]}")  # For 'Derek 71'

    # Loop through the nested lists
    for sub_item in item[2:]:
        # Format each sub-item
        name, score = sub_item[0], sub_item[1]
        print(f"{name} ={score}")  # For 'Xavier =80', etc.
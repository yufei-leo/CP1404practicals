# monster = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "pruple"]]
# scary_monster = [monster for monster in monster if monster[1] > 16]


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} ({self.age})"
# p1 = Person("Jane", 19)
# print(p1)
# people = [Person("Alexa", 21), Person("Siri", 25)]
# print(people)

# class Monster:
#
#     def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
#         self.name = name
#         self.number_of_teeth = number_of_teeth
#         self.colour = colour
#
#     def is_scary(self):
#         return self.number_of_teeth > 16 or self.colour.lower() == "red"
#
# print(Monster(name="Mike", number_of_teeth=4, colour="blue"))

class User:
    def __init__(self, name):
        self.name = name
        self.tacos = 5
        self.score = 0

    def give_a_taco(self, other_user):
        if self.tacos > 0:
            self.tacos -= 1
            other_user.tacos += 1
            self.score += 1
            print(f"{self.name} gave a taco to {other_user.name}.")
        else:
            print(f"{self.name} has no tacos left to give.")

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.tacos} tacos left"

user1 = User("Ben")
user2 = User("Jim")

print(user1)
user1.give_a_taco(user2)
print(user1)
print(user2)
# #  def life_in_weeks(age):
# #     age = int(input("What's your current age?"))
# #     years_remaining = 90 - age
# #     weeks_remaining = years_remaining * 2
# #     print(input(f"You have {weeks_remaining} weeks left."))
# #
# # life_in_weeks(12)
# name = input("Hello, what is your name?")
# location = input("Where're are you from?")
# def greet_with(name, location):
#     print("Hello" + " " + name)
#     print(f"What is it like in {location}?")
#
# greet_with("Eunice", "Imo" )
# # greet_with(name = "Eunice", location = "Imo")

def greet():
    name = input("Hi, What's your name?\n")
    weather = input(f"How's the weather over there, {name}\n")
    print(f"Hope to meet you sometime, {name} ")

greet()

# function that allows for input
def life_in_weeks(age):
    age = int(input("What's your current age?"))
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 2
    print(input(f"You have {weeks_remaining} weeks left."))
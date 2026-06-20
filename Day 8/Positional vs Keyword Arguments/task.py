# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#
#
# def greet(name, location):
# #     name = input("Hi! What's your name?")
# #     location = input("what's your location?")
#     print(f"Hi {name}")
#     print(f"How's the wether at {location}?")
#
# name = input("Hi! What's your name?")
# location = input("What location are you at?")
#
# greet(name, location)
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with("Smith", "America")

# fruits_list = ["apple", "banana", "cherry"]
# def letter_count():
#    text = "".join(fruits_list) #this case, you need "".join(...) because your data is a list of words,
    # while .count() for strings works on a single string. join() combines items in a list into one string.
    # fruits = ["apple", "banana", "cherry"]
    # text = "".join(fruits)
    # print(text). the empty string before the .join, acts as a separator.
#     a = text.count("a")
#     b =  text.count("b")
#     r =  text.count("r")
#     print(a, b, r)
#
# letter_count()

# print(fruits)

#
# def calculate_love_score(name1, name2):
#     combined = (name1 + name2).lower()
#
#     # TRUE letters
#     t = combined.count('t')
#     r = combined.count('r')
#     u = combined.count('u')
#     e_true = combined.count('e_true')
#
#     true_score = t + r + u + e_true
#
#     print(f"T occurs {t} times")
#     print(f"R occurs {r} times")
#     print(f"U occurs {u} times")
#     print(f"E occurs {e_true} times")
#     print(f"Total = {true_score}\n")
#
#     # LOVE letters
#     l = combined.count('l')
#     o = combined.count('o')
#     v = combined.count('v')
#     e_love = combined.count('e')
#
#     love_score = l + o + v + e_love
#
#     print(f"L occurs {l} times")
#     print(f"O occurs {o} times")
#     print(f"V occurs {v} times")
#     'Angela Yu', "Jack Bauer"
#     print(f"E occurs {e_love} times")
#     print(f"Total = {love_score}\n")
#
#     # Final score
#     final_score = int(str(true_score) + str(love_score))
#     print(f"Love Score = {final_score}")
#calculate_love_score("Angela Yu", "Jack Bauer")
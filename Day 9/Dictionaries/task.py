programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "National Band"
# print(programming_dictionary)
#
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary)

# To add a new entry into a dictionary, all you need to do is to tap into the dictionary.
# -  then using square brackets ([]), we define the key which in our case is Bug. after an equal sign,
# we get to assign the new value. afterwhich, we go ahead to print our programming dictionary.

programming_dictionary["gbb"] = "abc"
print(programming_dictionary)
empty_dictionary = {} # we use a set of calibrace to create an empty string

# We could also use a set of empty calibrace to wipe a dictionary. eg
programming_dictionary = {}
print(programming_dictionary)
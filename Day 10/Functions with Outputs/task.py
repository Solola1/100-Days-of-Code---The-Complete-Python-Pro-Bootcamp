def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
#what happens is this return output replaces the part of the code where the function was called

format_name("SoLomOn", "oLAmIdE")# which is this. You can still save it in a variable and print.
print(format_name("SoLomOn", "oLAmIdE")) #eg.

#The .title() method is a built-in Python string function that returns a copy of the string where
# the first character of every word is converted to uppercase, and all remaining characters in that word are forced into lowercase.
#word = "they're at the event".title()
#print(word)

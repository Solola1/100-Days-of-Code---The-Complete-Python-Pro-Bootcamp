def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
# Docstrings - Docstrings (documentation strings) are special string literals used
# directly after the definition of a Python module,
# function, class, or method to explain what the code do.
# And they start with """""" you write your documentation in-between these 3 quotation marks
#eg. def calculate_area(radius):
#    """Calculate and return the area of a circle."""
#    import math
#    return math.pi * (radius ** 2)




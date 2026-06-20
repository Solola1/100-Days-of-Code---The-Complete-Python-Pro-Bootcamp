bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # you can use this conversion to roundup to a whole number
print(round(bmi,2)) # In Python, the round() function is a built-in tool used to round a number to a specified number of decimal places or
# to the nearest integer. In this case, bmi = 84 / 1.65 ** 2 will = 31
# anything below 3 won't round up. eg, 3.3 = 3 but 3.5 upward = 4. print(round(bmi,2)) rounds it up to a floating point number with two decimal places

# In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")
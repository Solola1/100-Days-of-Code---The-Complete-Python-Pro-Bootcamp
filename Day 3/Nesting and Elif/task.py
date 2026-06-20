print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you?"))
if height >= 120: #This condition has to be true
    print("You can ride the rollercoaster")
    if age <= 12: # While this condition has to be false
        print("Your bill is $5.")
    elif age <= 18:
        print("Your bill is $7")
    else:
        print("Your bill is $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

import art
def add(n1, n2):
     return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary
# print(operations["*"](4, 8)) # You can get the name of the functions by tapping into the relevant key

while True:
    print(art.logo)
    num1 = float(input("What's the first number? "))
    continue_play = True
    while continue_play:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)# looping through this, it Shows which mathematical symbol would be used
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_play = input(f"Type 'y' to continue playing {answer}, or type 'n' to start a new calculation: ")

        if continue_play == "y":
            num1 = answer
        else:
            continue_playing = False
            print("\n" * 20)
            quit()





import calendar
# def is_leap_year(year):
#     year_divided = []
#     year = int(input("What year are you in?"))
#     if year % 4 == 0:
#         print("True")
#     else:
#         print("False")
# is_leap_year("2000")
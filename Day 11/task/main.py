import random
# def user_card():
#     num1 = random.randint(1, 11)
#     num2 = random.randint(1, 11)
#     sum = num1 + num2
#     ace = 10
#     print(f"user{num1, num2}")
#     print(f"user = {sum}")
#     if sum > 23:
#         print("You lost")
#     elif sum == user_card:
#         print("draw")
#     elif sum != 23:
#         responce = input("Type 'y' for another card and 'n' to tender\n")
#         print(responce)
#     if responce == "y":
#         new_num = random.randint(1, 11)
#         total = sum + responce
#         if total >= 23:
#           print(f"your final result is: {total}")
#
# user_card()
#
# def computer_card():
#     num1 = random.randint(1, 11)
#     num2 = random.randint(1, 11)
#     sum = num1 + num2
#     ace = 10
#     print(f"computer:{num1, num2}")
#     print(f"computer = {sum}")
#     if sum >= 23:
#         print("Computer lost")
#     elif sum == user_card:
#         print("draw")
#     elif sum != 23:
#         new_num = random.randint(1, 11)
#         print(new_num)
#
#
#
# computer_card()
#
#

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
for _ in range(2):# You use underscore (_) when you don't need a variable in a for loop. Maybe you just need the loop to run twice.we just added the underscore cus python syntax requires us to fill in something there that it can hold unto.
    new_card = deal_card()
    user_cards += new_card


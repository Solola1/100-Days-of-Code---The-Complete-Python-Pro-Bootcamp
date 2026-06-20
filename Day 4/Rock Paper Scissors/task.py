import random
hand = ["rock", "paper", "scissors"]
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = (rock, paper, scissors)


User_choice = int(input("What do you choos? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if User_choice >= 0 and User_choice <=2:
    print(game_image[User_choice])
computer_choice = random.randint(0,2)
print(f"The computer chose {computer_choice}.")
print(game_image[computer_choice])

if computer_choice == 0 and User_choice == 2:
    print("You win!")
if User_choice == 0 and computer_choice == 2:
    print("You loose!")
elif computer_choice > User_choice:
    print("You loose!")
elif User_choice >= 3 and computer_choice <= 2:
    print("Invalid input")
elif computer_choice == User_choice:
        print("It's a draw!")
else:
    print("OOps! You typed in a wrong input!")
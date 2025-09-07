import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


print("Welcome to dice rolling game.")

while True:
    user_choice = input("Roll the dice? (y/n): ")
    
    if user_choice.upper() == "Y":
        dice = roll_dice()
        print(dice)
    elif user_choice.upper() == "N":
        print("Thanks for playing.\nGoodbye!")
        break
    else:
        print("Invalid choise! Please try again...")

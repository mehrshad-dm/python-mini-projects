import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


print("Welcome to dice rolling game.")

times = -1
while times < 0:
    try:
        times = int(input("How many times do you want to roll the dice? "))
    except ValueError:
        print("Invalid number, please try again.")
        continue
    
while times > 0:
    user_choice = input("Roll the dice? (y/n): ")
    
    if user_choice.upper() == "Y":
        dice = roll_dice()
        print(dice)
        times -= 1
    elif user_choice.upper() == "N":
        print("Thanks for playing.\nGoodbye!")
        break
    else:
        print("Invalid choise! Please try again...")

import random


def rand_num(min, max):
    num = random.randint(min, max)
    return num


choice_max = int(input("Please enter the maximum: "))
choice_min = int(input("Please enter the minimum: "))

computer_number = rand_num(choice_min, choice_max)

while True:
    try:
        user_number = int(input(f"Guess the number between {choice_min} and {choice_max}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_number > computer_number:
        print("Too high!")
    elif user_number < computer_number:
        print("Too low!")
    elif user_number == computer_number:
        print("Congratulations! You guessed the number.")
        break

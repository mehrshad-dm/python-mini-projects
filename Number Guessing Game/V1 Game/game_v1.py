import random


def rand_num():
    num = random.randint(1, 100)
    return num


computer_number = rand_num()
while True:
    try:
        user_number = int(input("Guess the number between 1 and 100: "))
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

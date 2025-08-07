import random


def rand():
    computer_choice = random.choice(["sang", "kaghaz", "gheychi"])
    return computer_choice


def user():
    print("Yeki ra entekhab knid:")
    print("sang, kaghaz, gheychi")
    user_choice = input("Entekhab khod ra vared knid: ")
    return user_choice


def compare(computer_choice, user_choice):
    if computer_choice == user_choice:
        print(f"Har do {user_choice} ra entkhab kardid\n")
    elif (
        (user_choice == "sang" and computer_choice == "gheychi")
        or (user_choice == "kaghaz" and computer_choice == "sang")
        or (user_choice == "gheychi" and computer_choice == "kaghaz")
    ):
        print(f"Afrin,shuma barande shudid. entekhab computer {computer_choice} bod.\n")
    else:
        print(f"Motasefam,shuma barande nashudid. javab computer {computer_choice} bod.\n")


while True:
    user_choice = user()
    computer_choice = rand()
    compare(computer_choice, user_choice)

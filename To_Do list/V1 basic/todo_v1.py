tasks = []

print(
    " Hello dear, Welcome to To_Do list application.\n With this app, you can organize your tasks."
)
while True:
    print("What do you want?")
    print("1.add task\n2.remove task\n3.show task\n4.exit app")
    try:
        choose = int(input("Enter your choose (number): "))
    except ValueError:
        print("Please enter a valid number\n")
    if choose == 1:
        task = input("Write your task: ")
        tasks.append(task)
    elif choose == 2:
        for i, t in enumerate(tasks):
            print(f"{i}. {t}")
        try:
            rm = int(input("Which one do you want to remove (enter number)? "))
            if 0 <= rm < len(tasks):
                tasks.pop(rm)
            else:
                print("task not found")
        except ValueError:
            print("Please enter a valid number\n")
    elif choose == 3:
        print("your tasks:")
        for i, t in enumerate(tasks):
            print(f"{i}. {t}")
        print("\n")
    elif choose == 4:
        break

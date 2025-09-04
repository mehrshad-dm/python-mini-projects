def c_to_f(num):
    res = (num * 9 / 5) + 32
    return res


def f_to_c(num):
    res = (num - 32) * 5 / 9
    return res


def m_to_k(num):
    res = num / 1000
    return res


def k_to_m(num):
    res = num * 1000
    return res


print(
    " 1. Celsius to Fahrenheit\n 2. Fahrenheit to Celsius\n 3. Kilometers to Meters\n 4. Meters to Kilometers\n 5. Exit"
)

while True:
    try:
        choice = int(input("Enter your choice (just number): "))
    except ValueError:
        print("Oops! That doesn't look like a number. Try again with a valid number.")
        continue
    if choice == 5:
        print("Bye!")
        break
    elif choice < 1 or choice > 5:
        print("Invalid number, Please try again between 1-5.")
        continue
    try:
        input_value = float(input("Enter your number: "))
    except ValueError:
        print("Oops! That doesn't look like a number. Try again with a valid number.")
        continue
    if choice == 1:
        unit = "F"
        result = c_to_f(input_value)
    elif choice == 2:
        unit = "C"
        result = f_to_c(input_value)
    elif choice == 3:
        unit = "M"
        result = k_to_m(input_value)
    elif choice == 4:
        unit = "K"
        result = m_to_k(input_value)
    elif choice == 5:
        break
    else:
        print("Invalid number, Please try again.")
    print(f"The result is {result} {unit}.")
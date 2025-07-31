def is_greater(number_1, number_2):
    """
 Checks if number_1 is greater than number_2.
    Returns:
        True if number_1 > number_2
        "equal" if number_1 == number_2
        False if number_1 < number_2
    """
    if number_1 > number_2:
        return True
    elif number_1 == number_2:
        return "equal"
    else:
        return False


a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
result = is_greater(a, b)
if result is True:
    print(f"Number {a} is greater than {b}")
elif result == "equal":
    print(f"Number {a} and {b} are equal")
else:
    print(f"Number {a} is smaller than {b}")

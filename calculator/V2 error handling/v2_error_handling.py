"""
CLI Calculator with Error handling for divide.
--------------
A simple command-line calculator that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("number 2 can not be 0 in the divide")
    except Exception as e:
        print(f"another error: {e}")


print("🔢 Welcome to the CLI Calculator")
print("Choose an operation:")
print("  +  Addition")
print("  -  Subtraction")
print("  *  Multiplication")
print("  /  Division")

operation = input(" what do you want?")
number_1 = float(input("please enter number 1: "))
number_2 = float(input("please enter number 2: "))

if operation == "+":
    result = add(number_1, number_2)
elif operation == "-":
    result = subtract(number_1, number_2)
elif operation == "*":
    result = multiply(number_1, number_2)
elif operation == "/":
    result = divide(number_1, number_2)
else:
    result = "Invalid operation!"

print(f"the result is : {result}")

def calculate(a, b, what_to_do):

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def Exponentiation(a, b):
        return a**b

    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Second number can't be zero in the divide"

    if what_to_do == "multiply":
        return multiply(a, b)
    elif what_to_do == "add":
        return add(a, b)
    elif what_to_do == "divide":
        return divide(a, b)
    elif what_to_do == "Exponentiation":
        return Exponentiation(a, b)


result = calculate(4, 2, "Exponentiation")
print(result)

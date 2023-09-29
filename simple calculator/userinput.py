# Prompt user for input
from add import add
from calci import subtract, multiply, divide

user_input = input(": ")

if user_input == "quit":
     break
elif user_input in ("add", "subtract", "multiply", "divide"):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_input == "add":
        result = add(num1, num2)
    elif user_input == "subtract":
        result = subtract(num1, num2)
    elif user_input == "multiply":
        result = multiply(num1, num2)
    elif user_input == "divide":
        result = divide(num1, num2)

    print("Result:", result)
else:
    print("Invalid input. Please try again.")

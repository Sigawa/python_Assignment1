#Creating a calculator 
# Type first number
number1 = input("Type the first number: ")

# Type second number
number2 = input("Type the second number: ")

# Choose Operation desired (+, -, *, /)
operation = input("Type +, -, * or /: ")

# numbers to be converted to float
number1 = float(number1)
number2 = float(number2)

# To obtain answer for numbers and operation entered
if operation == "+":
    print(number1, "+", number2, "=", number1 + number2)
elif operation == "-":
    print(number1, "-", number2, "=", number1 - number2)
elif operation == "*":
    print(number1, "*", number2, "=", number1 * number2)
elif operation == "/":
    if number2 == 0:
        print("Can't divide by zero!")
    else:
        print(number1, "/", number2, "=", number1 / number2)
else:
    print("Please use +, -, *, or / only.")

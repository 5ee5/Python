number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")

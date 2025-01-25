#Python calculator
result = 0

operation = input("Type the operation that you will use:(+,-,*,/) ")
num1 = float(input("Type the first number: "))
num2 = float(input("Type the second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else:
    result = num1 / num2


print(f"The result is {result}")

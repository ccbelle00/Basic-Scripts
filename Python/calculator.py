# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("Select operation: add, subtract, multiply, divide")
choice = input("Enter choice: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "add":
    print(add(num1, num2))
elif choice == "subtract":
    print(subtract(num1, num2))
elif choice == "multiply":
    print(multiply(num1, num2))
elif choice == "divide":
    print(divide(num1, num2))
else:
    print("Invalid choice")

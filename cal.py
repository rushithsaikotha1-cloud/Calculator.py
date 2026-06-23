# Basic Calculator in Python

import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def Calculate_trig_function(angle, function):
    if function == 'sin':
        return math.sin(math.degrees(angle))
    elif function == 'cos':
        return math.cos(math.degrees(angle))
    elif function == 'tan':
        return math.tan(math.degrees(angle))
        if math.degrees(angle) == 90 and function == 'tan':
            return "The tan of 90 degrees is undefined"
    else:
        raise ValueError("Invalid function. Please choose 'sin', 'cos', or 'tan'.")
    
    
print("Select operation:")
print("A. Add")
print("S. Subtract")
print("M. Multiply")
print("D. Divide")
print("T. Trigonometric Functions")

choice = input("Enter choice (A/S/M/D/T): ")

if choice in ('A', 'S', 'M', 'D'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'A':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == 'S':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == 'M':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == 'D':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

else: 
    print("Trignometric function selected.")

if choice in ('T'):
    angle = float(input("Enter the angle in degrees: "))
    function = input("Enter the function (sin, cos, tan): ")
    try:
        result = Calculate_trig_function(angle, function)
        if math.degrees(angle) == 90 and function == 'tan':
            print("The tan of 90 degrees is undefined")
        print(f"The {function} of {angle} degrees is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")

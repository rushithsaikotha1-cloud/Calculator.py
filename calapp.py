import tkinter 

import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row, col = 0, 0

for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda x=button: click(x)

    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    root,
    text="Clear",
    font=("Arial", 16),
    command=clear
).pack(fill="both", padx=10, pady=10)

root.mainloop()

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

root = tk.Tk()
root.title("Trigonometry Calculator")
root.geometry("400x300")

title = tk.Label(root, text="Trigonometry Calculator", font=("Arial", 18))
title.pack(pady=10)

tk.Label(root, text="Enter Angle (Degrees)").pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Sin", width=10,
          command=lambda: calculate("sin")).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Cos", width=10,
          command=lambda: calculate("cos")).grid(row=0, column=1, padx=5)

tk.Button(frame, text="Tan", width=10,
          command=lambda: calculate("tan")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Clear", width=15,
          command=clear).pack(pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

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
        angle = float(input("Enter the angle in degrees: "))
    function = input("Enter the function (sin, cos, tan): ")
    try:
        result = Calculate_trig_function(angle, function)
        if math.degrees(angle) == 90 and function == 'tan':
            print("The tan of 90 degrees is undefined")
        print(f"The {function} of {angle} degrees is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
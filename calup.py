# Calculator Pro - A simple calculator with scientific functions using Tkinter

import tkinter as tk
import math

# ---------------- FUNCTIONS ---------------- #

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()

        result = eval(
            expression,
            {
                "__builtins__": None,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log": math.log10,
                "pi": math.pi,
            }
        )

        entry.delete(0, tk.END)
        entry.insert(0, round(result, 6))

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def trig(func):
    try:
        angle = float(entry.get())

        if func == "sin":
            result = math.sin(math.radians(angle))

        elif func == "cos":
            result = math.cos(math.radians(angle))

        elif func == "tan":
            if abs(angle % 180 - 90) < 0.0001:
                result = "Undefined"
            else:
                result = math.tan(math.radians(angle))

        entry.delete(0, tk.END)
        entry.insert(0, round(result, 6) if result != "Undefined" else result)

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, num ** 2)
    except:
        entry.insert(0, "Error")

def sqrt():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(num))
    except:
        entry.insert(0, "Error")

def log():
    try:
        num = float(entry.get())
        if num <= 0:
            entry.delete(0, tk.END)
            entry.insert(0, "Error: log undefined for non-positive numbers")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, math.log10(num))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Calculator Pro")
root.geometry("400x650")
root.configure(bg="#1e1e1e")

entry = tk.Entry(
    root,
    font=("Arial", 22),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
entry.pack(fill="both", padx=10, pady=10)

# ---------------- NORMAL BUTTONS ---------------- #

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

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
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=cmd
).grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1

# ---------------- SCIENTIFIC BUTTONS ---------------- #

frame = tk.Frame(root, bg="#201f1f")
trig_frame = tk.Frame(root, bg="#1e1e1e")
trig_frame.pack(pady=10)

tk.Button(
    trig_frame,
    text="Sin",
    width=8,
    font=("Arial", 12),
    bg="#333333",
fg="white",
activebackground="#555555",
activeforeground="white",
    command=lambda: trig("sin")
).grid(row=0, column=0, padx=5)

tk.Button(
    trig_frame,
    text="Cos",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: trig("cos")
).grid(row=0, column=1, padx=5)

tk.Button(
    trig_frame,
    text="Tan",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: trig("tan")
).grid(row=0, column=2, padx=5)

tk.Button(
    trig_frame,
    text="√",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=sqrt
).grid(row=1, column=0, pady=5)

tk.Button(
    trig_frame,
    text="x²",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=square
).grid(row=1, column=1, pady=5)

tk.Button(
    trig_frame,
    text="log",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: click("log(")
).grid(row=2, column=1, pady=5)

tk.Button(
    trig_frame,
    text="Clear",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=clear
).grid(row=1, column=2, pady=5)
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
 
tk.Button(
    trig_frame,
    text="π",
    width=8,
    font=("Arial", 12),
    bg="#333333", 
    fg="white",
    activebackground="#555555",
    activeforeground="white", 
    command=lambda: click("pi")
).grid(row=2, column=2, pady=5)


tk.Button(
    trig_frame,
    text="⌫",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=backspace
).grid(row=2, column=0, pady=5)

tk.Button(
    trig_frame,
    text="(",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    command=lambda: click("(")
).grid(row=3, column=0)

tk.Button(
    trig_frame,
    text=")",
    width=8,
    font=("Arial", 12),
    bg="#333333",
    fg="white",     
    activebackground="#555555",
    activeforeground="white",
    command=lambda: click(")")
).grid(row=3, column=1)


# ---------------- KEYBOARD BINDINGS ---------------- #

def key_press(event):
    key = event.char

    if key.isalnum() or key in "+-*/().":
        click(key)

    elif key == "\r":   # Enter key
        calculate()

    elif key == "\b":   # Backspace key
        backspace()
def calculate():
    try:
        expression = entry.get()

        expression = expression.replace("sin(", "math.sin(math.radians(")
        expression = expression.replace("cos(", "math.cos(math.radians(")
        expression = expression.replace("tan(", "math.tan(math.radians(")
        expression = expression.replace("sqrt(", "math.sqrt(")
        expression = expression.replace("log(", "math.log10(")
        expression = expression.replace("pi", str(math.pi))
        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, round(result, 6))

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error") 
       
root.bind("<Key>", key_press)
root.bind("<Delete>", lambda event: clear())
root.bind("<Return>", lambda event: calculate())

root.mainloop()
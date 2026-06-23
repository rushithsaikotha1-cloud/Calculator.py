import tkinter as tk
import math

def press(num):
    entry.insert(tk.END, str(num))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

def trig(func):
    try:
        angle = float(entry.get())
        angle = math.radians(angle)

        if func == "sin":
            result = math.sin(angle)
        elif func == "cos":
            result = math.cos(angle)
        elif func == "tan":
            result = math.tan(angle)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="x", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","+","="
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda x=button: press(x)

    tk.Button(frame, text=button, width=6, height=2,
              command=cmd).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="sin", width=10,
          command=lambda: trig("sin")).pack(pady=2)

tk.Button(root, text="cos", width=10,
          command=lambda: trig("cos")).pack(pady=2)

tk.Button(root, text="tan", width=10,
          command=lambda: trig("tan")).pack(pady=2)

tk.Button(root, text="Clear", width=10,
          command=clear).pack(pady=5)

root.mainloop()
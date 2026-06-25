import tkinter as tk
from tkinter import font as tkfont
import math
from enum import Enum

class ButtonType(Enum):
    NUMBER = "number"
    OPERATOR = "operator"
    FUNCTION = "function"
    CONTROL = "control"

class ModernCalculator:
    """Modern calculator application with scientific functions"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Pro")
        self.root.geometry("500x750")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        # Store expression and history
        self.expression = ""
        self.history = []
        
        # Create UI
        self._setup_styles()
        self._create_display()
        self._create_buttons()
        self._bind_keys()
        
    def _setup_styles(self):
        """Setup color scheme and fonts"""
        self.colors = {
            "bg": "#ffffff",
            "display_bg": "#FFFFFF",
            "number_btn": "#444242",
            "operator_btn": "#c47128",
            "function_btn": "#444444",
            "control_btn": "#555555",
            "text": "#0a0909",
            "hover": "#000000"
        }
        
        self.fonts = {
            "display": tkfont.Font(family="Arial", size=28, weight="bold"),
            "button": tkfont.Font(family="Arial", size=14, weight="bold"),
            "small": tkfont.Font(family="Arial", size=11)
        }
    
    def _create_display(self):
        """Create the display area"""
        display_frame = tk.Frame(self.root, bg=self.colors["bg"])
        display_frame.pack(fill="both", padx=10, pady=10)
        
        # History label
        self.history_label = tk.Label(
            display_frame,
            text="",
            font=self.fonts["small"],
            bg=self.colors["bg"],
            fg="#928F8F",
            justify="right"
        )
        self.history_label.pack(fill="x", anchor="e")
        
        # Main display
        self.display = tk.Entry(
            display_frame,
            font=self.fonts["display"],
            justify="right",
            bg=self.colors["display_bg"],
            fg=self.colors["text"],
            insertbackground=self.colors["text"],
            border=0,
            state="readonly"
        )
        self.display.pack(fill="both", ipady=15)
    
    def _create_buttons(self):
        """Create all calculator buttons"""
        # Button layout
        layout = [
            [("Clear", "control"), ("⌫", "control"), ("(", "function"), (")", "function"), ("π", "function")],
            [("Sin", "function"), ("Cos", "function"), ("Tan", "function"), ("√", "function"), ("x²", "function")],
            [("7", "number"), ("8", "number"), ("9", "number"), ("/", "operator"), ("log", "function")],
            [("4", "number"), ("5", "number"), ("6", "number"), ("*", "operator"), ("←", "control")],
            [("1", "number"), ("2", "number"), ("3", "number"), ("-", "operator"), ("C", "control")],
            [("0", "number"), (".", "number"), ("=", "operator"), ("+", "operator"), ("History", "control")]
        ]
        
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(fill="both", padx=10, pady=10, expand=True)
        
        self.buttons_dict = {}
        
        for row_idx, row in enumerate(layout):
            button_frame.grid_rowconfigure(row_idx, weight=1)
            
            for col_idx, (text, btn_type) in enumerate(row):
                button_frame.grid_columnconfigure(col_idx, weight=1)
                
                btn = self._create_button(
                    button_frame, text, btn_type,
                    row_idx, col_idx
                )
                self.buttons_dict[text] = btn
    
    def _create_button(self, parent, text, btn_type, row, col):
        """Create a single button"""
        button_colors = {
            "number": self.colors["number_btn"],
            "operator": self.colors["operator_btn"],
            "function": self.colors["function_btn"],
            "control": self.colors["control_btn"]
        }
        
        # Command mapping
        command_map = {
            "Clear": self.clear,
            "⌫": self.backspace,
            "C": self.clear,
            "←": self.backspace,
            "=": self.calculate,
            "History": self.show_history,
            "Sin": lambda: self.apply_function("sin"),
            "Cos": lambda: self.apply_function("cos"),
            "Tan": lambda: self.apply_function("tan"),
            "√": lambda: self.apply_function("sqrt"),
            "x²": lambda: self.apply_function("square"),
            "log": lambda: self.apply_function("log"),
            "π": lambda: self.insert_value("pi"),
            "(": lambda: self.insert_value("("),
            ")": lambda: self.insert_value(")"),
        }
        
        # If not in map, it's a number or operator to insert
        if text not in command_map:
            command = lambda: self.insert_value(text)
        else:
            command = command_map[text]
        
        btn = tk.Button(
            parent,
            text=text,
            font=self.fonts["button"],
            bg=button_colors.get(btn_type, self.colors["number_btn"]),
            fg=self.colors["text"],
            activebackground=self.colors["hover"],
            activeforeground=self.colors["text"],
            command=command,
            border=0,
            highlightthickness=0
        )
        
        btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        return btn
    
    def insert_value(self, value):
        """Insert value into expression"""
        self.expression += str(value)
        self._update_display()
    
    def backspace(self):
        """Remove last character"""
        self.expression = self.expression[:-1]
        self._update_display()
    
    def clear(self):
        """Clear the display"""
        self.expression = ""
        self._update_display()
    
    def apply_function(self, func_name):
        """Apply mathematical functions"""
        try:
            value = float(self.expression) if self.expression else 0
            
            functions = {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": lambda x: math.sqrt(x) if x >= 0 else None,
                "square": lambda x: x ** 2,
                "log": lambda x: math.log10(x) if x > 0 else None,
            }
            
            result = functions[func_name](value)
            
            if result is None:
                self._set_error("Math Error")
            else:
                self.expression = str(round(result, 10))
                self.history.append(f"{func_name}({value}) = {self.expression}")
                self._update_display()
                
        except (ValueError, ZeroDivisionError):
            self._set_error("Invalid Input")
    
    def calculate(self):
        """Calculate the expression"""
        if not self.expression:
            return
        
        try:
            # Create safe namespace for eval
            safe_dict = {
                "__builtins__": {},
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log": math.log10,
                "pi": math.pi,
            }
            
            result = eval(self.expression, safe_dict)
            self.history.append(f"{self.expression} = {result}")
            self.expression = str(round(result, 10))
            self._update_display()
            
        except (SyntaxError, NameError, ZeroDivisionError):
            self._set_error("Syntax Error")
        except Exception as e:
            self._set_error("Error")
    
    def _update_display(self):
        """Update the display with current expression"""
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        
        # Show expression or '0' if empty
        display_text = self.expression if self.expression else "0"
        self.display.insert(0, display_text)
        self.display.config(state="readonly")
        
        # Update history hint
        if self.history:
            self.history_label.config(text=self.history[-1])
    
    def _set_error(self, message):
        """Display error message"""
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, message)
        self.display.config(state="readonly")
        self.expression = ""
    
    def show_history(self):
        """Show calculation history in a new window"""
        if not self.history:
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("History")
        history_window.geometry("300x300")
        history_window.configure(bg=self.colors["bg"])
        
        # Scrollbar
        scrollbar = tk.Scrollbar(history_window)
        scrollbar.pack(side="right", fill="y")
        
        # Listbox
        listbox = tk.Listbox(
            history_window,
            bg=self.colors["display_bg"],
            fg=self.colors["text"],
            yscrollcommand=scrollbar.set,
            border=0,
            font=self.fonts["small"]
        )
        listbox.pack(fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=listbox.yview)
        
        # Add history items
        for item in self.history[-20:]:  # Show last 20 items
            listbox.insert(tk.END, item)
        
        listbox.yview(tk.END)
    
    def _bind_keys(self):
        """Bind keyboard shortcuts"""
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<BackSpace>", lambda e: self.backspace())
        self.root.bind("<Escape>", lambda e: self.clear())
        
        # Number and operator keys
        for i in range(10):
            self.root.bind(str(i), lambda e, x=i: self.insert_value(x))
        
        for op in "+-*/.":
            self.root.bind(op, lambda e, x=op: self.insert_value(x))
        
        self.root.bind("(", lambda e: self.insert_value("("))
        self.root.bind(")", lambda e: self.insert_value(")"))

def main():
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

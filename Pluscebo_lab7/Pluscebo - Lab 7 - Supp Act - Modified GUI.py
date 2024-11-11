import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.configure(bg='light blue')

        self.result = tk.StringVar()
        self.history = []
        self.create_widgets()

    def create_widgets(self):
        #Input fields
        tk.Label(self.master, text="Enter first number:", bg='light blue', font=('Arial', 10)).grid(row=0, column=0, padx=15, pady=5)
        self.entry1 = tk.Entry(self.master, font=('Arial', 10))
        self.entry1.grid(row=0, column=1, padx=15, pady=5)

        tk.Label(self.master, text="Enter second number:", bg='light blue', font=('Arial', 10)).grid(row=1, column=0, padx=15, pady=5)
        self.entry2 = tk.Entry(self.master, font=('Arial', 10))
        self.entry2.grid(row=1, column=1, padx=15, pady=5)

        #Buttons for operations
        button_config = {'bg': 'pink', 'font': ('Arial', 8)}

        tk.Button(self.master, text="Add", command=self.add, **button_config).grid(row=2, column=0, padx=15, pady=10)
        tk.Button(self.master, text="Subtract", command=self.subtract, **button_config).grid(row=2, column=1, padx=15, pady=10)
        tk.Button(self.master, text="Multiply", command=self.multiply, **button_config).grid(row=3, column=0, padx=15, pady=10)
        tk.Button(self.master, text="Divide", command=self.divide, **button_config).grid(row=3, column=1, padx=15, pady=10)
        tk.Button(self.master, text="Square Root", command=self.square_root, **button_config).grid(row=4, column=0, padx=15, pady=10)
        tk.Button(self.master, text="Exponent", command=self.exponent, **button_config).grid(row=4, column=1, padx=15, pady=10)
        tk.Button(self.master, text="Sin", command=self.sin, **button_config).grid(row=5, column=0, padx=15, pady=10)
        tk.Button(self.master, text="Cos", command=self.cos, **button_config).grid(row=5, column=1, padx=15, pady=10)
        tk.Button(self.master, text="Tan", command=self.tan, **button_config).grid(row=6, column=0, padx=15, pady=10)
        tk.Button(self.master, text="Clear", command=self.clear, **button_config).grid(row=6, column=1, padx=15, pady=10)

        #Label to show result
        tk.Label(self.master, text="Result:", bg='light blue', font=('Arial', 10)).grid(row=7, column=0, padx=15, pady=15)
        self.result_label = tk.Label(self.master, textvariable=self.result, bg='light blue', font=('Arial', 10))
        self.result_label.grid(row=7, column=1, padx=15, pady=15)

        #History display
        tk.Label(self.master, text="History:", bg='light blue', font=('Arial', 10)).grid(row=8, column=0, padx=15, pady=15)
        self.history_display = tk.Text(self.master, height=10, width=30, state='disabled', font=('Arial', 10))
        self.history_display.grid(row=8, column=1, padx=15, pady=15)

    def add(self):
        self.perform_operation(lambda x, y: x + y, "+")

    def subtract(self):
        self.perform_operation(lambda x, y: x - y, "-")

    def multiply(self):
        self.perform_operation(lambda x, y: x * y, "*")

    def divide(self):
        self.perform_operation(lambda x, y: x / y, "/")

    def square_root(self):
        try:
            num1 = float(self.entry1.get())
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number.")
            result = math.sqrt(num1)
            self.result.set(result)
            self.history.append(f"√{num1} = {result}")
            self.update_history()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def exponent(self):
        self.perform_operation(lambda x, y: x ** y, "^")

    def sin(self):
        try:
            num1 = float(self.entry1.get())
            result = math.sin(math.radians(num1))
            self.result.set(result)
            self.history.append(f"sin({num1}) = {result}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def cos(self):
        try:
            num1 = float(self.entry1.get())
            result = math.cos(math.radians(num1))
            self.result.set(result)
            self.history.append(f"cos({num1}) = {result}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def tan(self):
        try:
            num1 = float(self.entry1.get())
            result = math.tan(math.radians(num1))
            self.result.set(result)
            self.history.append(f"tan({num1}) = {result}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def perform_operation(self, operation, symbol):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            if symbol == "/" and num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = operation(num1, num2)
            self.result.set(result)
            self.history.append(f"{num1} {symbol} {num2} = {result}")
            self.update_history()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except ZeroDivisionError as e:
            messagebox.showerror("Math Error", str(e))

    def clear(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result.set("")
        self.history.clear()
        self.update_history()

    def update_history(self):
        self.history_display.config(state='normal')
        self.history_display.delete(1.0, tk.END)  #Clear text area
        for entry in self.history:
            self.history_display.insert(tk.END, entry + "\n")
        self.history_display.config(state='disabled')  #Read-only

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
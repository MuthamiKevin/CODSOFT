import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected!")

        result_label.config(text=f"Result: {result}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except ZeroDivisionError as zde:
        messagebox.showerror("Error", str(zde))

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create entry boxes for numbers
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(window)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Create a dropdown menu for operations
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_dropdown = tk.OptionMenu(window, operation_var, *operation_choices)
operation_dropdown.grid(row=0, column=2, padx=5, pady=5)
operation_var.set("+")  # Set default operation to addition

# Create a button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()

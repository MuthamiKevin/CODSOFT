import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        password_label.config(text="Please enter a valid password length.")
        return

    complexity = complexity_var.get()
    if complexity == "Low":
        chars = string.ascii_letters
    elif complexity == "Medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(password_length))
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Create dropdown for complexity
complexity_label = tk.Label(window, text="Complexity:")
complexity_label.grid(row=1, column=0, padx=5, pady=5)

complexity_var = tk.StringVar()
complexity_choices = ["Low", "Medium", "High"]
complexity_dropdown = tk.OptionMenu(window, complexity_var, *complexity_choices)
complexity_dropdown.grid(row=1, column=1, padx=5, pady=5)
complexity_var.set("Medium")  # Set default complexity

# Create button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create label to display generated password
password_label = tk.Label(window, text="")
password_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

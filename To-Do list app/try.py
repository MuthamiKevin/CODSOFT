import tkinter as tk

def fill_entry(value):
    current_text = entry.get()
    cursor_position = entry.index(tk.INSERT)
    new_text = current_text[:cursor_position] + value + current_text[cursor_position:]
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

window = tk.Tk()
window.title("Entry Box Fill Example")

entry = tk.Entry(window)
entry.pack()

button_fill_1 = tk.Button(window, text="Fill 1", command=lambda: fill_entry("1"))
button_fill_1.pack()

button_fill_2 = tk.Button(window, text="Fill 2", command=lambda: fill_entry("2"))
button_fill_2.pack()

window.mainloop()

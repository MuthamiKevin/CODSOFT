import tkinter as tk
from tkinter import messagebox

def mark_as_done():
    selected_index=listbox.curselection()
    if not selected_index:
        messagebox.showwarning("warning!", "Please selsct a task to mark as done.")
    else:
        confirmation=messagebox.askyesno("Confirmation", "Are you sure yhou want to mark this task as done?")
        if confirmation:
            task=listbox.get(selected_index)
            task_done = task + " ✔"
            listbox.delete(selected_index)
            listbox.insert(selected_index, task_done)
            

def update_task():
    selected_index = listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning!", "Please select a task to update.")
    else:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to edit this task?")
        if confirmation:
            new_text = entrybox.get()
            listbox.delete(selected_index) 
            listbox.insert(selected_index, new_text)  
            items[selected_index[0]] = new_text
            entrybox.delete(0, tk.END)  
            update_numbers()

        

def delete():
    selected=listbox.curselection()
    if not selected: 
        messagebox.showwarning("Warning", "Please select a task to delete.")
    else:
        selected_item = listbox.get(selected)
        response = messagebox.askyesno("Confirmation", f"Are you sure you want to delete '{selected_item}'?")
        if response:  
            listbox.delete(selected[0]) 
       

def add_task():
    text = entrybox.get()
    entrybox.delete(0, tk.END)
    if text == "":
        messagebox.showwarning(title="Warning!", message="Please Enter a new task.")
    else:
        listbox.insert(tk.END, text)
        messagebox.showinfo("Info", "Task added to the list.")
        
        items.append(text)  
        update_numbers()  

def update_numbers():
    listbox.delete(0, tk.END) 
    for i, item in enumerate(items, start=1):
        listbox.insert(tk.END, f"{i}. {item}")

window = tk.Tk()
window.title("To-Do list App")
window.geometry('450x500')
window.resizable(0, 0)

frame_app = tk.Frame(window)
frame_app.place(x=50, y=50)

listbox = tk.Listbox(frame_app, height=15, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

tasklabel = tk.Label(window, text="Add new task here.")
tasklabel.place(x=5, y=5)

entrybox = tk.Entry(window)
entrybox.place(x=15, y=25)
entrybutton = tk.Button(window, width=15, text="Add new task", command=add_task)
entrybutton.place(x=150, y=20)

items = [] 

update_button = tk.Button(window, width=15, text="Update task",command=update_task)
update_button.place(x=15, y=300)

delete_button = tk.Button(window, width=15, text="Delete task", command=delete)
delete_button.place(x=15, y=350)

mark_button = tk.Button(window, width=15, text="Mark task as done", command= mark_as_done)
mark_button.place(x=15, y=400)

window.mainloop()

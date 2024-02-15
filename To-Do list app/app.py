import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(master, textvariable=self.task_var)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

def main():
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

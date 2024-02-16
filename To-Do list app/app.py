import tkinter as tk
from tkinter import *
import tkinter.messagebox

def add_task():
    text=entrybox.get()
    entrybox.delete(0, tk.END)
    if text=="":
        tk.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
    else:
        listbox.insert(END ,text)
        tk.messagebox.showinfo("Info", "Task added to the list.")
        
window=tk.Tk()
window.title("To-Do list App")
window.geometry('450x500')
window.resizable(0,0)

frame_app=Frame(window)
frame_app.place(x=50,y=50)
listbox=Listbox(frame_app, height=15,width=50)
listbox.pack(side=tk.LEFT)

scrollbar=Scrollbar(frame_app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


tasklable=tk.Label(window, text="Add new task here.")
tasklable.place(x=5,y=5)

entrybox=tk.Entry(window)
entrybox.place(x=15,y=25)
entrybutton=tk.Button(window, width=15, text="Add new task", command=add_task)
entrybutton.place(x=150,y=20)

update_button=tk.Button(window, width=15, text="Update task")
update_button.place(x=15,y=300)

delete_button=tk.Button(window, width=15, text="Delete task")
delete_button.place(x=15,y=350)

mark_button=tk.Button(window, width=15, text="Mark task as done")
mark_button.place(x=15, y=400)
window.mainloop()
from tkinter import *
import random
import string
import pyperclip
from tkinter import messagebox

root = Tk()
root.geometry("400x280")
root.title("Password Generator")
root.resizable(0,0)

title = StringVar()
label = Label(root, textvariable=title)
label.place(x=8,y=5)
title.set("The strength of the password:")

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection)
R1.place(x=5,y=25)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection)
R2.place(x=5,y=45)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection)
R3.place(x=5,y=65)

labelchoice = Label(root)
labelchoice.place(x=5,y=5)

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel)
lentitle.place(x=5,y=85)

val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlenght.place(x=5,y=105)

def callback():
    if choice.get() == 0:
        messagebox.showwarning("Warning", "Please select the strength of the password.")
    else:
        password = passgen()
        lsum.config(text=password)
        pyperclip.copy(password)

passgenButton = Button(root, text="Generate Password", bd=5, command=callback, pady=3)
passgenButton.place(x=5,y=145)

def copy_callback():
    password = lsum.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

copyButton = Button(root, text="Copy to Clipboard", bd=5, command=copy_callback, pady=3)
copyButton.place(x=150, y=145)

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
         return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
         return "".join(random.sample(advance, val.get()))

root.mainloop()

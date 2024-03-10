from tkinter import *

def fill_entry(value):
    global equation_text
    equation_text = equation_text + str(value)
    entry_box.delete(0, END)
    entry_box.insert(END, equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        entry_box.delete(0, END)
        entry_box.insert(END, total)
        equation_text = total
    except SyntaxError:
        entry_box.delete(0, END)
        entry_box.insert(END, "syntax error")
        equation_text = ""
    except ZeroDivisionError:
        entry_box.delete(0, END)
        entry_box.insert(END, "arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    entry_box.delete(0, END)
    equation_text = ""

window = Tk()
window.title("Calculator App")
window.geometry("300x300")

equation_text = ""
entry_box = Entry(window, font=('consolas',20), bg="white", width=18)
entry_box.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=2, width=4, font=35, command=lambda: fill_entry(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=2, width=4, font=35, command=lambda: fill_entry(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=2, width=4, font=35, command=lambda: fill_entry(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=2, width=4, font=35, command=lambda: fill_entry(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=2, width=4, font=35, command=lambda: fill_entry(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=2, width=4, font=35, command=lambda: fill_entry(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=2, width=4, font=35, command=lambda: fill_entry(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=2, width=4, font=35, command=lambda: fill_entry(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=2, width=4, font=35, command=lambda: fill_entry(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=2, width=4, font=35, command=lambda: fill_entry(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=2, width=4, font=35, command=lambda: fill_entry('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=2, width=4, font=35, command=lambda: fill_entry('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=2, width=4, font=35, command=lambda: fill_entry('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=2, width=4, font=35, command=lambda: fill_entry('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=2, width=4, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=2, width=4, font=35, command=lambda: fill_entry('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=2, width=12, font=35, command=clear)
clear.pack()

window.mainloop()

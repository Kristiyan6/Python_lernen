import random
import pyperclip
from tkinter import *
from tkinter.ttk import *


def low():
    entry.delete(0, END)
    lenght = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, lenght):
            password = password + random.choice(lower)
            return password
    elif var.get() == 0:
        for i in range(0, lenght):
            password = password + random.choice(upper)
            return password
    elif var.get() == 3:
        for i in range(0, lenght):
            password = password + random.choice(digits)
            return password
    else:
        print("Wähle eine option aus.")


def generate():
    password1 = low()
    entry.insert(1, password1)


def copy1():
    random_passwort = entry.get()
    pyperclip.copy(random_passwort)


root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Passwort Generator")
Random_passwort = Label(root, text="Passwort")
Random_passwort.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
copy_button = Button(root, text="Kopieren", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generieren", command=generate)
generate_button.grid(row=0, column=3)

radio_low = Radiobutton(root, text="Leicht", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Schwer", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()

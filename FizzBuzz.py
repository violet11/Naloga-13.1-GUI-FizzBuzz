# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *

# okno

window = Tk()
window.resizable(width=False, height=False)
window.geometry('{}x{}'.format(640, 480))

# pozdrav
pozdrav = Label(window, text = "Izberi število med 1 in 100", fg="blue", font=(None, 22))
pozdrav.pack()


# entry
guess = Entry(window)
guess.pack()

import tkMessageBox


def check_guess():
    iskano_stevilo = int(guess.get())
    for x in range(1,  iskano_stevilo + 1):
        if x % 3 == 0 and x % 5 == 0:
            result_text = "FizzBuzz"

        elif x % 5 == 0:
            result_text = "buzz"

        elif x % 3 == 0:
            result_text = "fizz"

        else:
            result_text = str(x)

        tkMessageBox.showinfo("Result", result_text)

# submit button
import Tkinter
submit = Tkinter.Button(window, text="Submit", fg="blue", command=check_guess)
submit.pack()


window.mainloop()
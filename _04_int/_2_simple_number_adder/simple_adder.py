"""
* Write a Python program that asks the user for two numbers.


* Display the sum of the two numbers to the user
"""

from tkinter import simpledialog

import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

question = simpledialog.askinteger('Title', "What number would you like to pick?")
question1 = simpledialog.askinteger('Title', "What number would you like to pick?")

print(question + question1 )




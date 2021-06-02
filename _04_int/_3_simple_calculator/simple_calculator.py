"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()



question1= simpledialog.askinteger('Title', "What number would you like to pick?")
question2 = simpledialog.askinteger('Title', "What number would you like to pick?")

question3 = simpledialog.askstring('Title', "Would you like to add,subtract,multiply, or divide?")

if question3 == 'add':
    print(question1+question2)

elif question3 == 'subtract':
    print(question1-question2)

elif question3 == 'multiply':
    print(question1*question2)

elif question3 == 'divide':
    print(question1/question2)




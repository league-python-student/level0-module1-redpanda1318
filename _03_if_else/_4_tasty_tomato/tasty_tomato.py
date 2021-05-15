from tkinter import *
from tkinter import simpledialog, Tk, messagebox
import tkinter as tk

window = Tk()
window.withdraw()

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
color = simpledialog.askstring('Title', "What color tomato would you like? (red, blue, or green)")
#    You can give them up to three choices
if color == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

elif color == 'green':
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="brown", outline="")

elif color == 'blue':
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")


# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato







root.mainloop()

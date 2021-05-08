# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math
from tkinter import simpledialog, Tk, messagebox

window = Tk()
window.withdraw()


radius = simpledialog.askinteger('Title', "What should the radius of the circle be?")

area = radius * radius * math.pi

circumference = 2 * radius * math.pi
item = simpledialog.askstring('Title', "Would you like to calculate the area or the circumference of a circle?")
if item == 'area':
    print('The area is: ' + str(area))


elif item == 'circumference':
    print('The circumference is: ' + str(circumference))





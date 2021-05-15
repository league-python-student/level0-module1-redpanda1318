import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    thing = turtle.Turtle()
    
    # Ask the user what shape they want to draw and store it in a variable
    question = simpledialog.askstring('Title', "What shape do you want to draw?(square,triangle, or rectangle")
    # Draw the shape requested by the user using if-elif-else statements
    if question == 'square':
        thing.forward(100)
        thing.right(90)
        thing.forward(100)
        thing.right(90)
        thing.forward(100)
        thing.right(90)
        thing.forward(100)

    elif question == 'triangle':
        thing.forward(100)
        thing.right(60)
        thing.forward(100)
        thing.right(60)



    # Call the turtle .done() method

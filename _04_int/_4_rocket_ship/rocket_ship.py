from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#9184e0")
canvas.grid()


# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#9184e0")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # This defines the x and y coordinated of all three points
    # of a triangle
    points = [x,y,x-80,y+90,x+80,y+90]
    canvas.create_polygon(points, fill='#3d3938', width=2) # draws triangle
    
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.
    canvas.create_oval(x-70,y+85,x+70,y+180, fill='yellow')
    canvas.create_oval(x-50,y+60,x+55,y+160,fill='orange')
    canvas.create_oval(x-20 ,y+50,x+40,y+140,fill='red')




    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()

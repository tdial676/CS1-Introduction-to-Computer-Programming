"""
Thierno Diallo

Lab5 part B question 2
"""
from tkinter import *

def draw_square(canvas, color, length, position):
    """
    This function takes four arguments for creating a square and creates 
    that square and returns it's handle.

    Arguments:
        - a canvas created from the class canvas containing the dimessions
        of the canvas we are drawing in.
        - a string color
        - an int length
        - a tuple (x,y) for position
    Return Value:
        - a handle string
    """
    (x1, y1) = position
    half = length/2
    handle = canvas.create_rectangle((x1 - half), (y1 - half), (x1 + half)
                                   , (y1 + half), fill=color, outline=color)
    return handle


if __name__ == '__main__':
    #Sets up window and canvas
    root = Tk()
    root.geometry('900x900')
    canvas = Canvas(root, width=900, height=900)
    canvas.pack()
    
    # Draws four squares
    draw_square(canvas,'orange', 150, (75,75))
    draw_square(canvas,'green', 150, (825,75))
    draw_square(canvas, 'blue', 150, (75,825))
    draw_square(canvas, 'black', 150, (825,825))

    #initializes infinite event loop
    root.mainloop()

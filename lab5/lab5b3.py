"""
Thierno Diallo

Lab5B question 3
"""
from tkinter import *
from lab5a import random_size, random_coords, random_color
from lab5b2 import draw_square


def key_handler(event):
    """
    This function quits the window.

    Arguments:
        - tkinter event
    Return Value: None
    """
    quit()


if __name__ == '__main__':
    #Sets up window and canvas
    root = Tk()
    root.geometry("900x900")
    canvas = Canvas(root, width=900, height=900)
    canvas.pack()

    #draws 30 random squares
    for num in range(30):
        draw_square(canvas, random_color(), random_size(30, 150)
                    , random_coords(900, 900))
    
    # quits when q is pressed
    root.bind('<q>', key_handler)

    #initializes infitnite event loop
    root.mainloop()

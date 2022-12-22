"""
Thierno Diallo

Lab5B question 1

This module draws four squares of diffrent colors at the 
cornors of our canvas.
"""
from tkinter import *

#Sets up window and canvas
root = Tk()
root.geometry('900x900')
c = Canvas(root, width=900, height=900)
c.pack()

#The Four squares drawn
sq_1 = c.create_rectangle(0, 0, 150, 150, fill='orange', outline= 'orange')
sq_2 = c.create_rectangle(750, 0, 900, 150, fill='green', outline= 'green')
sq_3 = c.create_rectangle(0, 750, 150, 900, fill='blue', outline= 'blue')
sq_4 = c.create_rectangle(750, 750, 900, 900, fill='black', outline= 'black')

#initializes infinite event loop
root.mainloop()


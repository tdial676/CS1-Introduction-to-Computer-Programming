"""
Thierno Diallo

Lab5 part A
"""
import random

#1a
def random_size(int_1, int_2):
    """
    This function takes two even ints and returns an even number between them.
    Arguments:
        - an even int (int_1)
        - an even int (int_2)
    Return Value: an even int
    """
    if int_1 >= 0 and int_1 <= int_2 and int_1 % 2 ==0 and int_2 % 2 == 0:
        num = random.randint(int_1 / 2, int_2 / 2) * 2
        return num
    else:
        return


#2a
def random_coords(max_x, max_y):
    """
    This function takes two numbers and returns the a tuple of coodinates
    between each number.

    Argument: 
        - an int (max_x)
        - an int (max_y)
    Return Value: a tuple (x,y)
    """
    if max_x >= 0 and max_y >= 0:
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        return(x, y)
    else:
        return


#3a
def random_color():
    """
    This function takes no arguments and returns a color value str.

    Arguments: None
    Return Value: a string
    """
    color = '#'
    for num in range(0,6):
        color += random.choice('0123456789ABCDEF')
    return color

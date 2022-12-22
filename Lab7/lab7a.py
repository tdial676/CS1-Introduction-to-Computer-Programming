"""
Thierno Diallo

Lab7a Pitfalls
"""

#A1
""" 
Stopping and quitting the entire program if a single doesnt exists is too
drastic and worst than what default python does as this method does not let
the user know the error location and type thus making it really hard to fix
or even identify.
"""

#A2
"""
While betters, this version still fails to let the user know which key was 
invalid thus in a big dictionary this error manage is not that useful for
fixing the error.
"""

#A3
"""
This code is unneccessary as it does the same thing as python would if 
there is a value error thus this code is irrelevant.
"""
def sum_of_key_values(data, key1, key2):
    """Returns sum of the values in the data dict stored at key1 and key2."""
    try:
        return data[key1] + data[key2]
    except KeyError:   # raised if a key isn't in a dictionary
        if key1 not in data:
            print(f'Key ({key1}) not found!')
        if key2 not in data:
            print(f'Key ({key2}) not found!')

#A4
"""
The error is being raised before the print statement stating what the error is
thus the print statement letting the user know what the error is will never be
printed. Also, this would be a value error not a type error as values less 
than zero are valid types.
"""

#A5
"""
This is incorrect as it raises a type error which is false considering their
error description because numbers less than or equal to zero are still 
either int or float types thus this error is misleading. It should be a value 
error because the function doesnt consider values below or equal to zero.
"""

#A6
"""
This method is too broad as it raises the the exceptipn but does not tell
the user the error type thus it can benefit from being more specific.
"""
from math import exp
def exp_x_over_x(x):
    """
    Return the value of e**x / x, for x > 0.0.

    e = 2.71828... is the base of natural logarithms.
    """
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

    
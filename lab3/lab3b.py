"""
Thierno Diallo

CS 1 lab3b
"""


#A1
"""
There is no spacing between the operators. There is no spacing between the arguments.
the naming of the function isn't helpful because it does not tell us what the function doe.
The code is also very repetitive. (not a style error)
Adding () will also make it a lot easier to read the code. (not a style error)
"""
def sums_of_three_cubes(a, b, c):
    return (a ** 3) + (b ** 3) + (c ** 3)


#A2
"""
The naming of the the function and arguments should be lower case with underscores.
There are line breaks after operators.
Needs () around return value if it's going to spam over numerous line
Spelling error in the comment, which should also be a doc string. Comment is also incomprehensable.
The return values should be alligned with the other return values
The code is also very repetitive and violates our DRY principle (not a style error)
"""
def sumofcubes(argument_a, argument_b, argument_c, argument_d):
    """
    This fucntion takes a,b,c and returns the sum of the cubes of a, b, and c.
    """
    return (argument_a ** 3
            + argument_b ** 3
            + argument_c ** 3
            + argument_d ** 3)


#A3
""""
The second return statement is not indented correctly.
The first statement is over indented.
There is no space between the two functions
Not a style error but the code is very repeatetive
Adding () will also make it a lot easier to read the code. (not a style error)
"""
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return (x ** 3) + (y ** 3) + (z ** 3)


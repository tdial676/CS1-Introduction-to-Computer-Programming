#B.1 9 - 5 ---> 3
#B.1 4 * 2.5 ---> 10
#B.1 101 / 2 ---> 50
#B.1 101 / -2 ---> -51
#B.1 100 % 2 ---> 1
#B.1 100 % 2 ---> -1
#B.1 -101 % 2 ---> 1
#B.1 101 / -2.0 ---> 50.5
#B.1 3 + 4 * 5 ---> 23
#B.1 (3 + 4) * 5 ---> 35

#B.2 x = 120 ---> x = 120
#B.2 x = x+ 1= ---> x = 130
#B.2 x += 20 ---> x = 150
#B.2 X = x - 30 ---> x = 120
#B.2 x -=70 ---> x = 50
#B.2 x *=3 ---> x = 150
#B.2 x /= 5 ---> x = 30
#B.2 x %= 5 ---> x = 0

#B.4 1j + 2.4j ---> 3.4j
#B.4 4j * 4j ---> (-16 + 0j)
#B.4 (1 + 2j)/(3 + 4j) ---> (0.44 + 0.08j)
#B.4 (1 + 2j) * (1 + 2j) ---> (-3 + 4j)
#B.4 1 + 2j * 1 + 2j ---> (1 + 4j)
#B.4 They give diffrent results because of the order of operations which requires that the multiplication operation take precedence over addtion.
    # +This tells us that python handles complex numbers as variables because all the answers contained the variable j.

#B.3 x += x - x
# Pyhton evaluates the follwing expression as x = x+x-x. First it grabs the original x value. Then it adds thjat value to itself. Then it subtracts the orginal x from the that sum.


#B.5 cmath.sin(-1.0 + 2.0j) ---> (-3.165778513216168 + 1.959601041421606j)
#B.5 cmath.log(-1.0 + 3.4j) ---> (1.2652585805200263 + 1.856847768512215j)
#B.5 cmath.exp(-cmath.pi * 1.0j) ---> (-1-1.2246467991473532e - 16j)
"""
It is better to use "import math" and "import cmath" compared to importing all because they have similar 
function calls thus this way allows us to dissern from which module we are calling a function from. 
For example, they both have the srqt call, however only cmath can take the square root of negative 
numbers, thus we want python to specifically use the sqrt function from cmath when attempting to 
find the square root of nagative numbers instead of the math module which will give us an error.
"""
#B.6 "foo" + 'bar' ---> 'foobar'
#B.6 "foo" 'bar' ---> 'foobar'
#B.6 a = 'foo'; b = "bar"; a + b ---> 'foobar'
#B.6 a = 'foo'; b = "bar"; a  b ---> SyntaxError: invalid syntax
#B.6 month = "October"; days = 31; days + " days hath " + month ---> TypeError: unsupported operand type(s) for +: 'int' and 'str'

#B.7 "A\nB\nC"

#B.8 s = 70 * '_'

#B.9 'Line 1\nLine 2\nLine 3'

#B.10 is bellow:
x = 9
y = 4.25
print('Lorem is {}.'.format(x))
print('Lorem is {} months old.'.format(x))
print('A puppuccino is {}.'.format(y))
print('{} * {}'.format(y,x))
print('{} * {} is 38.25.'.format(y,x))
#end of B.10.

#B.11 is below:
num = float(input("Enter a number: "))
print(num)
#B.11 End

#B.12 is below:
def quadratic(a,b,c,x):
    val1 = a*(x**2)
    val2 = b*x
    val3 = c
    return val1 + val2 + val3
#B.12 Ends

#B.13 is below:
def GC_content(DNA):
    """""
    This function takes a string argument and returns the percent reaccurace of certain letters.

    Argument: 'DNA' (a string)
    Return value: a float value of the perecnt of T and G in the the DNA string.
    """""
    concentrationG = float(DNA.count('G'))
    concentrationC = float(DNA.count('C'))
    total = concentrationC + concentrationG
    ratio = total / len(DNA)
    return ratio
#B.13 ends
    
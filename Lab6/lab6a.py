"""
Thierno Diallo

Lab 6 Part A
"""


#A1
"""
The else statement is uneccessary as we can just 
return false if the if statement returns nothing.
"""
def is_positive(x):
    """Return `True` if `x` is positive."""
    if x > 0:
        return True
    return False


#A2
"""
The location and bool are uneccessary. Also, we dont need
the second if and else staments as we can just return -1 if
the if statement does not return anything.
"""
def find(x, lst):
    for i, e in enumerate(lst):
        if e == x:
            return i
    return -1


#A3
"""
Replace the if statements with elif so that it doesnt check all
the if statements. Also, we can replace the last elif statement
with else because that is the only possible case.
"""
def categorize(x):
    """Return a string categorizing the integer `x`."""
    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x > 0 and x < 10:
        category = 'small'
    else:
        category = 'large'
    return category


#A4
"""
We dont need to check the lenth of the list because that can be tedious.
Also, we dont need to consider indivdual cases when we can make a general
answer for a list of any length thus we can remove all of the condtionals
and loop through the list adding each number to the sum, which is initially 0
thus it will return zero for an empty list.
"""
def sum_list(lst):
    """Return the sum of the elements of a list of numbers."""
    answer = 0
    for num in lst:
        answer += num
    return answer


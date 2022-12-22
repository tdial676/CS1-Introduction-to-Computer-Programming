#B1a
"""
The if statement should be 'if a == 0' because a single = will asign a value to 'a' rather than 
check whether the statement is true or false.
"""

#B1b
"""
You should not add an identifier to the argument thus the definition should be 'def add_suffix(s):'
without putting the argument s in quotation marks.
"""

#B1c
"""
There should not be any quotations around the s in the return statement because then the function
will return 's-Caltech' rather than the value of s + '-Caltech'. The correct format would be: s + '-Caltech'.
"""

#B1d
"""
This is invalid syntax because to add values to a list we use the .append() method thus it should be lst.append('bam').
Also, you can only add lists to other lists thus you can also fix it by using the following: lst + ['bam'].
"""

#B1e
"""
This will return nothing because you are asking the computer to return a method. Also, the .reverse() method already changes 
the list so we don't need to redefine it as lst2.
"""

#B1f
"""
This will give a syntax error because they are trying to append a list onto a list instead they should add the 2 lists:
letters + list. 
"""

#B2
"""
The program sets the value of 'a' as 10 and the value of 'b' as 20 before adding the two values to form 'c'. lastly, it changes 
the value of 'a' after doing the operation and before printing 'c' thus c = 30.
"""

#B3
"""
n = 2 * add_and_double_1(1, 2, 3) would work because the function evaluates and gives you back a value that you can manupulate.
n = 2 * add_and_double_2(1, 2, 3) would not work because the function is not giving you back any value. Rtaher it is just
evaluating. The return gives us back a value while print just shows us the value.
"""

#B4
"""
n = 2 * sum_of_squares_1(2, 3) will work because the function takes two arguments where as n = 2 * sum_of_squares_2(2, 3)
will no work because you are giving the function two arguments when it doesnt take any arguments.
"""

#B5
"""
This will not work because strings are immutable.
"""

#B6
"""
This will not work because none of the values being doubled are being stored.
"""
import pytest
import random

#A1
def complement(DNA):
    """
    This function takes one str argument and returns the compliment of that str.

    argument: DNA (a string)
    Return value: The complement of the DNA string sequence
    """
    DNA_complement = ''
    for letter in DNA:
        if letter == 'A':
            DNA_complement += 'A'
        elif letter == 'C':
            DNA_complement += 'C'
        elif letter == 'T':
            DNA_complement += 'U'
        elif letter == 'G':
            DNA_complement += 'G'
    return  DNA_complement

#A2           
def list_complement(dna):
    """
    This function takes a list of a DNA sequence and turns it into a list of the complement sequence .

    Argument: A string list of a DNA sequence 
    Return Value: Has no return value
    """
    pos = 0
    for letter in dna:
        if letter == 'A':
            dna[pos] = 'T'
            pos +=1
        elif letter == 'C':
            dna[pos] = 'G'
            pos +=1
        elif letter == 'T':
            dna[pos] = 'A'
            pos +=1
        elif letter == 'G':
            dna[pos] = 'C'
            pos +=1

#A3
def product(sequence):
    """
    This fuction takes a list of numbers and returns the product of all the numbers in that list. 
    For an empty list, it will return 1.

    Argument: an int list
    Return Value: an int product of all the numbers in the list
    """
    total = 1
    for num in sequence:
        total = num * total
    return total

#A4
def factorial(positive_int):
    """
    This function takes a positive int and returns the factorial of that number.

    Argument: a positive int
    Return Value: the factoral of the argument as an int 
    """
    return product(list(range(1, positive_int + 1, 1)))

#A5
def dice(m, n):
    """
    This function takes in two int inputs(sides of a die and number of rolls) and returns 
    the sum of all rolls.

    Argument: two ints. One representing the sides of the die(m) and the other, representing the number of rolls(n)
    Returrn Value: an int sum of all the rolls.
    """
    z = 1
    sum = 0
    while z <= n: 
     sum += (random.choice(range(1, m, 1)))
     z += 1
    return sum

#A6
def remove_all(int_lst, value):
    """
    This function takes a list of ints and one value, then returns the list without that value in it.

    Arguments: a list of ints and the value we want to remove from the list.
    Return Value: the argument list, but without the value we wanted to remove.
    """
    while int_lst.count(value) > 0:
        int_lst.remove(value)
    return int_lst

#A7
def remove_all2(int_lst, value):
    """
    This function takes a list of ints and one value, then returns the list without that value in it.

    Arguments: a list of ints and the value we want to remove from the list.
    Return Value: the argument list, but without the value we wanted to remove.
    """
    appearance = int_lst.count(value)
    for num in range(appearance):
        int_lst.remove(value)

def remove_all3(int_lst, value):
    """
    This function takes a list of ints and one value, then returns the list without that value in it.

    Arguments: a list of ints and the value we want to remove from the list.
    Return Value: the argument list, but without the value we wanted to remove.
    """
    while value in int_lst:
        int_lst.remove(value)
    return int_lst

#A8
def any_in(lst1, lst2):
    """
    This function takes in two lists and returns a boolean stating true if the two lists
    have atleast one shared element and false otherwise.

    Argument: Two lists 
    Return Value: A boolean stating True if the lists share any elements and False otherwise.
    """
    for num in lst1:
        if num in lst2:
            return True
        else:
            return False
holder = "UGCGACUACUUUUCUACAAGGAAUCAGACUUCUCCGACUC"
print(len(holder))
print(complement("ACGCTGATGAAAAGATGTTCCTTAGTCCGAAGAGGCTGAG"))
"Arg pro gly "
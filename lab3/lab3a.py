"""
Thierno Diallo

CS 1 lab3a
"""


#A1
def list_reverse(nums_lst):
    """
    This function takes a list and returns the reverse of the list as a new list
    without changing the original.

    Argument: a list 
    Return value: a new list containing the reverse of the argument list
    """
    lst2 = nums_lst[:]
    lst2.reverse()
    return lst2


#A2
def list_reverse2(lst):
    """
    This function takes a list and returns the reverse of the list as a new list
    without changing the original.

    Argument: a list 
    Return value: a new list containing the reverse of the argument list
    """
    lst2 = []
    for num in range(-1, -len(lst)-1, -1):
        lst2.append(lst[num])
    return lst2


#A3
def file_info(file_name):
    """
    This function takes a file and returns the number of lines, words, 
    and charecters in the file.

    Arguments: str file name
    Return Value: a tuple containing the number of lines, words, 
    and charecters in the file
    """
    file = open(file_name)
    total_lines = 0
    total_words = 0
    total_chars = 0

    while True:
        line = file.readline
        if not line:
            break
        total_lines +=1
        total_words += len(line.split())
        total_chars += len(line)
    file.close()
    return (total_lines, total_words, total_chars)


#A4
def file_info2(file_name):
    """
    This functions takes a file and returns a dictionary of the number 
    of lines, words, and charecters.

    Argument: str file name
    Return Value: a dictionary containing the number of lines, words, 
    and charecters in the file.
    """
    (total_lines, total_words, total_chars) = file_info(file_name)
    dictionary = {'line_count': total_lines, 'word_count': total_words,
                  'character_count': total_chars}
    return dictionary


#A5
def longest_line(file_name):
    """
    This function takes a file and returns the length of the largest 
    line in the file and its location.

    Argument: str file name
    Return Value: a tuple containing the longest line number and its length.
    """
    file = open(file_name)
    largest_line = ''
    line_number = 0
    largest_line_number = 0
    for line in file:
        line_number +=1
        if len(line) >= len(largest_line):
            largest_line = line
            largest_line_number = line
    file.close()
    return (largest_line_number, largest_line)


#A6 
def count_fns(file_name):
    """
    This function takes a file and returns the number of functions in that file.

    Arguments: str file name
    Return Value: int value representing the number of functions in the file.
    """
    file = open(file_name)
    function_nums = 0
    for line in file:
        if line[0:4] == 'def ':
            function_nums +=1
    file.close()
    return function_nums


#A7
def tabs_to_spaces(file_name, tab_spaces):
    """
    This function takes a file name and the desired number of spaces, and 
    writes a new file with all the tabs replaced with the desired number 
    of spaces.

    Arguments: a str file name and an int desired number of spaces
    Return Value: no return value
    """
    file = open(file_name, 'r')
    new_file = open('spaced_' + file_name, 'w')
    tabbed_lines = 0
    replaced_tabs = 0
    str = ''
    for line in file:
        if '\t' in line:
            tabbed_lines += 1
            while '\t' in line:
                line = line.replace('\t', tab_spaces * ' ', 1)
                replaced_tabs += 1
        str += line
    new_file.write(str)
    file.close()
    new_file.close()
    print(f'Lines with tabs: {tabbed_lines}\nTotal replaced: {replaced_tabs}')


#A8
"""
1*(2**7) + 0*(2**6) + 1*(2**5) + 1*(2**4) + 0*(2**3) + 1*(2**2) + 0*(2**1) + 1*(2**0)
= 128 + 0 + 32 + 16 + 0 + 4 + 0 +1
= 128 + 32 + 16 + 4 + 1
= 181

The largest eight-digit binary number in decimal would be 0b11111111
which would be:
1*(2**7) + 1*(2**6) + 1*(2**5) + 1*(2**4) + 1*(2**3) + 1*(2**2) + 1*(2**1) + 1*(2**0)
= 255 in decimal
"""


#A9
def binary_to_decimal(lst):
    """
    This function takes a list of binary numbers and coverts them to decimal.

    Argument: an int list of binary numbers
    Return Value: an int value in decimal
    """
    sum = 0
    for i,e in enumerate(lst):
        sum += 2 ** ((len(lst) - 1) - i) * e
    return sum


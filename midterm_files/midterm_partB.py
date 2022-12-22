"""
Thierno Diallo

Midterm_PartB
"""


#B.1
def special_sums(n):
    """
    This function takes an int and retruns the min and max sum of 
    n ints ranging from 1-9 as a tuple

    Argument: an int n
    Return Value: a tuple (min, max)
    """
    if n in range(1, 10):
        min = sum(range(1, n + 1))
        max = sum(range(9, 9 - n, -1))
        return (min, max)


#B.2
def remove_consecutive_dups(lst):
    """
    This function takes a list and removes all consecutive duplicates
    in that list.

    Arguments: as list lst
    Return Value: None
    """
    count = 0
    while count < len(lst) - 1:
        if lst[count] == lst[count + 1]:
            del lst[count]
        else:
            count += 1


#B.3
def to_snake_case(str):
    """
    This function takes a string and returns a new string of the original
    in snake case.

    Arguments: a string (str)
    Return Value: a string
    """
    final_str = ''
    for i,letter in enumerate(str):
        if letter.isupper() == False:
            final_str += letter
        elif i != 0 and i != len(str) - 1:
            final_str += '_' + letter.lower()
        else:
            final_str += letter.lower()
    return final_str


#B.4
def format_fn_header(fn_name, lst_args):
    """
    This function takes a function name and a list of arguments and returns
    a string of the inputs as a function.

    Arguments:
        - a str fn_name
        - a list lst_args
    Return Value: a string funtcion
    """
    fn = to_snake_case(fn_name)
    args = '(' + ', '.join(lst_args) +')'
    function = f'def {fn}{args}:'
    return function
    

#B.5
def generate_args_data():
    """
    This funtion takes no arguments and returns a dictionary of user 
    input arguments.

    Arguments: None
    Return Value: A dictionary of argument inputs
    """
    args = {}
    while True:
        arg_name = input('Add an argument name (press <return> for none): ')
        arg_name = to_snake_case(arg_name)
        if arg_name != '':
            arg_type = input(f'What is the expected type of `{arg_name}`? ')
            if arg_type == '':
                arg_type = 'unspecified'
            arg_dscrptn = input(f'Description of `{arg_name}`: ')
            args[arg_name] = (arg_type, arg_dscrptn)
        else:
            return args


#B.6
def generate_return_data():
    """
    This function takes no arguments and returns a tuple containing the 
    return value type input and the return value input.

    Arguments: None
    Return Value: A tuple containing type and return value
    """
    type = input('What is the expected type of the return? ')
    if type == '':
        type = 'unspecified'
    return_value = input('Description of return: ')
    return(type, return_value)


#B.7
def print_fn_stub(fn, arg_dict, val_tuple, description):
    """
    This function takes four arguments describing the parts of a funtion and
    returns correctely formatted function string.

    Arguments:
        - str function name (fn)
        - a dictionary of arguments (arg_dict)
        - a tuple for return value type and value (val_tupe)
        - a str deecription of the function (description)
    Return Value
    """
    func_name = format_fn_header(fn, arg_dict)
    if val_tuple[1] == '':
        return_value = f'({val_tuple[0]})'
    else:
        return_value = f'({val_tuple[0]}): {val_tuple[1]}'
    arguments = ''
    for arg in arg_dict:
        if arg_dict[arg][1] == '':
            arguments += f'`{arg}` ({arg_dict[arg][0]}) {arg_dict[arg][1]}\
 \n    '
        else:
            arguments += f'`{arg}` ({arg_dict[arg][0]}): {arg_dict[arg][1]}\
\n    '
    if arg_dict == {}:
        arguments = ''
    print(f'''{func_name}\n  """\n  {description}\n\n  Arguments:\n
    {arguments}\n\n  Returns:\n    {return_value}\n  """\n  pass''')
  
  

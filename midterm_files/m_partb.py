"""

"""

def special_sums(n):
    """
    """
    if n in range(1, 10):
        min = sum(range(1, n + 1))
        max = sum(range(9, 9 - n, -1))
        return (min, max)


def remove_consecutive_dups(lst):
    """
    """
    count = 0
    while count < len(lst) - 1:
        if lst[count] == lst[count + 1]:
            del lst[count]
        else:
            count += 1


def to_snake_case(str):
    """
    """
    final_str = ''
    for i,letter in enumerate(str):
        if letter.isupper() == False:
            final_str += letter
        elif i != 0 and i != len(str) - 1:
            final_str += '-' + letter.lower()
        else:
            final_str += letter.lower()
    return final_str


def format_fn_header(fn_name, lst_args):
    """
    """
    fn = to_snake_case(fn_name)
    args = '(' + ', '.join(lst_args) +')'
    function = f'def {fn}{args}:'
    return function
    

def generate_args_data():
    args = {}
    while True:
        arg_name = input('Add an argument name (press <return> for none): ')
        arg_name = to_snake_case(arg_name)
        if arg_name != '':
            arg_type = input(f'What is the expected type of `{arg_name}`: ')
            if arg_type == '':
                arg_type = 'unspecified'
            arg_dscrptn = input(f'Description of `{arg_name}`: ')
            args[arg_name] = (arg_type, arg_dscrptn)
        else:
            return args


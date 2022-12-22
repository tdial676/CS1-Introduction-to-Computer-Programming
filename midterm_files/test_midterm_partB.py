"""
Author: El Hovik
Version: 11/04/21

Helper tests for students on the 21fa midterm.
These should be used to catch subtle bugs/edge cases; you
_may_ ask how to interpret a test error on Discord/OH but 
_may not_ get help from anyone
solving a problem otherwise (ask El if you're unsure).
"""

# Needed to import all functions from student solutions
# without qualifying for pytest purposes; refer to lecture
# on why import * is ok in this case (but usually not otherwise)
from midterm_partB import * 
# This added import is a requirement for overriding print/input
# to test output/input on io functions
import midterm_partB

# B.1.
def test_special_sums():
  assert special_sums(1) == (1, 9)
  assert special_sums(2) == (3, 17)
  assert special_sums(3) == (6, 24)
  assert special_sums(4) == (10, 30)
  assert special_sums(8) == (36, 44)
  assert special_sums(9) == (45, 45)
  # None should be returned if n < 1 or > 9
  assert special_sums(0) is None
  assert special_sums(10) is None


# B.2.
def test_remove_consecutive_dups():
  nums = [1, 2, 3, 3, 2, 2, 1]
  test_ret = remove_consecutive_dups(nums)
  #  B.2. should not return anything
  assert test_ret is None
  assert nums == [1, 2, 3, 2, 1]
  lst = ['a', 'a']
  remove_consecutive_dups(lst)
  assert lst == ['a']
  nums = [1, 1]
  remove_consecutive_dups(nums)
  assert nums == [1]
  lst = []
  remove_consecutive_dups(lst)
  assert lst == []
  lst = [1, 1, '1', '1']
  remove_consecutive_dups(lst)
  assert lst == [1, '1']
  lst = [1, '1', 1]
  remove_consecutive_dups(lst)
  assert lst == [1, '1', 1]
  lst = ['', '', '']
  remove_consecutive_dups(lst)
  assert lst == ['']


# B.3.
def test_to_snake_case():
  # snek_case unchanged
  assert to_snake_case('snek_case') == 'snek_case'
  # Java... Classic.
  assert to_snake_case('camelCase') == 'camel_case'
  # starting uppercase ch C should be lowercase, otherwise c_
  assert to_snake_case('PascalCase') == 'pascal_case'
  # ignore nums
  assert to_snake_case('removeAll3') == 'remove_all3'
  assert to_snake_case('123') == '123'
  # Caterpillar beats leaf. Python beats caterpillar. 
  assert to_snake_case('cAtTeRpIlLaRcAsE') == 'c_at_te_rp_il_la_rc_ase'
  # empty case
  assert to_snake_case('') == ''
  # example from spec
  assert to_snake_case('FooBAR') == 'foo_b_ar'


# B.4.
def test_format_fn_header():
  # example from spec, 2-fully specified int args
  fn_name = 'dice'
  args = {'n': ('int', 'Number of dice to roll (>= 1)'),
          'm': ('int', 'Number of sides per dice (>= 1)')}
  fn_header = format_fn_header(fn_name, args.keys())
  assert fn_header == 'def dice(n, m):'

  # example from spec, 1 int arg specified, no description
  fn_name = 'factorial'
  args = {'n': ('int', '')}
  fn_header = format_fn_header(fn_name, args.keys())
  assert fn_header ==  'def factorial(n):'

  # example from spec, 0 args specified
  # requires to_snake_case to be correct
  fn_name = 'sayHello'
  args = {}
  fn_header = format_fn_header(fn_name, args.keys())
  assert fn_header == 'def say_hello():'


def gen_args_io_helper(capsys, input_values, prompts, exp_args):
  # test program assertion, not affected by student code 
  assert len(input_values) % 3 == 1
  arg_count = len(input_values) // 3
  # Essentially, this multiplies the 3-line prompts
  # depending on number of expected processed argument
  # in user prompting, then adds the first prompt as the final
  # prompt (when the user quits by giving '')
  prompts = (prompts[:3] * arg_count) + [prompts[0]]
  for i in range(len(input_values)):
    if i % 3 == 0:
      # each time we get a new argument from user, change
      # the expected argument name in subsequent two prompts
      # this argument name should be in snake_case in student
      # code and surrounded by `` as shown in examples
      snake_cased_arg_name = to_snake_case(input_values[i])
    if '{}' in prompts[i]:
      # replace `{}` with snake_cased name when referring 
      # to arg in prompt
      prompts[i] = prompts[i].format(snake_cased_arg_name)

  # override user input, capture values
  def mock_input(s):
    print(s, end='')
    next_input = input_values[0]
    del input_values[0]
    return next_input

  # override input function to catch it
  midterm_partB.input = mock_input
  args = generate_args_data()
  assert args == exp_args

  out, err = capsys.readouterr() 
  # fix new line differences in capsys call
  assert out.replace('\n', '') == ''.join(prompts).replace('\n', '')
  assert err == '' # no error expected


# B.5.
def test_generate_args_data(capsys):
  # Example from spec; 1 round of arg prompts with camelCased fn name
  input_values = ['dnaString', 'str', 'DNA sequence', '']
  prompts = ['Add an argument name (press <return> for none): ',
             'What is the expected type of `{}`? ',
             'Description of `{}`: ',
             'Add an argument name (press <return> for none): ']
  # generate_args_data should use to_snake_case
  expected_args = {'dna_string': ('str', 'DNA sequence')}
  gen_args_io_helper(capsys, input_values, prompts, expected_args)

  # Testing emtpy inputs
  input_values = ['']
  expected_args = {}
  gen_args_io_helper(capsys, input_values, prompts, expected_args)

  # Testing 2 rounds of fully-specified inputs
  input_values = ['dnaString', 'str', 'DNA sequence', 'base', 'str', 
                  'Single-character nucleotide base', '']
  expected_args = {'dna_string': ('str', 'DNA sequence'), 
                   'base': ('str', 'Single-character nucleotide base')}
  gen_args_io_helper(capsys, input_values, prompts, expected_args)

  # Testing 1 round of provided arg name with no type/desc
  input_values = ['n', '', '', '']
  # Empty type -> 'unspecified', empty description -> ''
  expected_args = {'n': ('unspecified', '')}
  gen_args_io_helper(capsys, input_values, prompts, expected_args)


# This could be refactored bit, but WIP duties call...
def gen_ret_io_helper(capsys, input_values, prompts, expected_ret):
  assert len(input_values) % 2 == 0
  # override user input, capture values
  def mock_input(s):
    print(s, end='')
    next_input = input_values[0]
    del input_values[0]
    return next_input

  # override input function to catch it
  midterm_partB.input = mock_input
  ret_data = generate_return_data()
  assert ret_data == expected_ret

  out, err = capsys.readouterr() 
  # fix new line differences in capsys call
  assert out.replace('\n', '') == ''.join(prompts).replace('\n', '')
  assert err == '' # no error expected


# B.6.
def test_generate_return_data(capsys):
  # These prompts don't use any previous input (different than B.5.)
  prompts = ['What is the expected type of the return? ',
             'Description of return: ']
             
  # Testing fully-specified return
  # inputs = [<type>, <desc>]
  inputs = ['float', 'Percentage of `base` in `dna_string` (0.0 to 100.0).']
  gen_ret_io_helper(capsys, inputs, prompts, tuple(inputs))
  # Testing return with only type specified (empty desc -> '')
  inputs = ['float', '']
  gen_ret_io_helper(capsys, inputs, prompts, ('float', ''))
  # Testing return with unspecified type and desc (empty type -> 'unspecified')
  inputs = ['', '']
  gen_ret_io_helper(capsys, inputs, prompts, ('unspecified', ''))
  # Testing with unspecified type, specified description
  inputs = ['', 'Who knows...']
  gen_ret_io_helper(capsys, inputs, prompts, ('unspecified', 'Who knows...'))


# B.7.
def test_print_fn_stub():
  # Testing dice example from spec
  fn_name = 'dice'
  args = {'n': ('int', 'Number of dice to roll (>= 1)'),
          'm': ('int', 'Number of sides per dice (>= 1)')}
  ret_data = ('int', 'Sum of `n` randomly-rolled `m`-sided dice.')
  fn_desc = 'Simulates `n` randomly-rolled `m`-sided dice, returning the sum of all rolls.'
  output = []
  # Override output for testing print statements
  midterm_partB.print = lambda s='' : output.append(s + '\n')
  print_fn_stub(fn_name, args, ret_data, fn_desc)
  fn_stub = '' + \
"""def dice(n, m):
  \"\"\"
  Simulates `n` randomly-rolled `m`-sided dice, returning the sum of all rolls.

  Arguments:
    `n` (int): Number of dice to roll (>= 1)
    `m` (int): Number of sides per dice (>= 1)

  Returns:
    (int): Sum of `n` randomly-rolled `m`-sided dice.
  \"\"\"
  pass
"""
  assert fn_stub == ''.join(output)

  # Testing foobar example from spec; -1 for sad docstring :(
  fn_name = 'FooBAR'
  args = {'c_at_er_pi_ll_ar': ('unspecified', '')}
  ret_data = ('dict', '')
  fn_desc = 'Who knows...'

  fn_stub = '' + \
"""def foo_b_ar(c_at_er_pi_ll_ar):
  \"\"\"
  Who knows...

  Arguments:
    `c_at_er_pi_ll_ar` (unspecified)

  Returns:
    (dict)
  \"\"\"
  pass
"""
  output = []
  print_fn_stub(fn_name, args, ret_data, fn_desc)
  assert fn_stub == ''.join(output)
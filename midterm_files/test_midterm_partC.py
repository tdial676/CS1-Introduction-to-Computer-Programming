"""
Author: El Hovik
Version: 11/07/21

Helper tests for students on the 21fa midterm.
These should be used to catch subtle bugs/edge cases; you
_may_ ask how to interpret a test error on Discord/OH but 
_may not_ get help from anyone
solving a problem otherwise (ask El if you're unsure).
"""

# Needed to import all functions from student solutions
# without qualifying for pytest purposes; refer to lecture
# on why import * is ok in this case (but usually not otherwise)
from midterm_partC import * 
# This added import is a requirement for overriding print/input
# to test output/input on io functions
import midterm_partC
# Make sure you have the example game data from midterm_files.zip in the same
# directory as this testing program
from partC_dummy_data import example_game_data
# time module is used to test runtime of get_game_data
import time


# C.1.
def test_get_game_data():
  # Tests that student function works for showid = 4
  # which is equivalent to provided dummy data
  show4_data = get_game_data(4)
  # Students should not be using isinstance of type(...) in their
  # solutions, but it is good for testing purposes. A tuple,
  # not a list, should be returned.
  assert isinstance(show4_data, tuple)

  # Should be 3 components of tuple
  assert len(show4_data) == 3

  airdate, show_count, game_data = show4_data

  # Tests that correct airdate is retrieved
  assert airdate == example_game_data[0]

  # Asserts that correct row count is retrieved for game data.
  # In this case 25, but may differ for other showids
  assert show_count == example_game_data[1]
  assert game_data == example_game_data[2]

  # Showid of 6 has 6 categories, 27 questions (edge case)
  airdate, show_count, game_data = get_game_data(6)
  assert airdate == '1984-09-20'
  assert show_count == 27
  assert len(game_data) == 6

  # First-game case
  t1 = time.time()
  airdate, show_count, game_data = get_game_data(1)
  t2 = time.time()
  assert airdate == '1984-09-10'
  assert show_count == 22
  assert len(game_data) == 5
  # Should stop processing data once showid=2 is found as hinted
  # at in spec.  
  show1_time = t2 - t1 # execution time in seconds

  # Last-game case; this one has 6 categories instead of 5
  # If this test takes a long time, student probably has nested loops/other
  # inefficient solutions.
  t1 = time.time()
  airdate, show_count, game_data = get_game_data(3639)
  t2 = time.time()
  show2_time = t2 - t1  # execution time in seconds
  assert airdate == '2012-01-27'
  assert show_count == 29
  assert len(game_data) == 6
  assert t2 - t1 < 2 # shouldn't take more than 2 seconds to run
  # if fails, re-run once more
  # if your machine is slow, can bump it up a bit but double-check
  # that you don't have unnecessary loops/calls 

  # Rough check to make sure that show1 time
  # is shorter than show2_time by a reasonable amount
  # if fails, re-run once more
  assert show2_time * 0.7 > show1_time 
  

# C.2.
def test_print_column_header(capsys):
  # Examples from spec
  columns = ['ANIMALS', 'COMPUTER SCIENCE', 'CSV', 'POKEMON']
  test_ret = print_column_header(columns)
  assert test_ret is None # should not have any return here.
  test_out = capsys.readouterr().out
  assert test_out =="""ANIMALS | COMPUTER SCIENCE | CSV | POKEMON
------------------------------------------\n"""
  # Example using provided dummy data (showid = 4)
  game_data = example_game_data[2]
  columns = game_data.keys() # pass columns as list of keys, not dict
  print_column_header(columns)
  test_out = capsys.readouterr().out
  assert test_out == """GEOGRAPHY | BY THE NUMBERS | TOYS & GAMES | TRANSPORTATION | FLOWERS & TREES | TRIVIA
-------------------------------------------------------------------------------------\n"""


# C.3.
def test_dict_to_table(capsys):
  # Examples from spec
  simple_data = {'CAT_A': {'100': ('Q', 'A'), '300': ('Q', 'A')},
                 'CAT_B': {'100': ('Q', 'A'), '200': ('Q', 'A'), '300': ('Q', 'A')}}
  # 2D list should work for n != 5 
  table = dict_to_table(simple_data, 3)
  test_out = capsys.readouterr().out
  assert not test_out # nothing should be printed by function
  assert table ==[['100', '100'], ['---', '200'], ['300', '300']]

  table = dict_to_table(simple_data, 4)
  assert table == [['100', '100'], ['---', '200'], ['300', '300'], ['---', '---']]

  # Testing with provided dummy data next
  game_data = example_game_data[2]
  table = dict_to_table(game_data, 5)
  assert table == [['100', '100', '100', '100', '100', '100'], 
                   ['200', '200', '200', '200', '200', '200'], 
                   ['300', '300', '300', '---', '---', '300'], 
                   ['400', '400', '400', '---', '---', '400'], 
                   ['500', '500', '500', '500', '---', '500']]

  # Testing one other 6-category example from showid = 6
  game_data = get_game_data(6)[2]
  table = dict_to_table(game_data, 5)
  assert table == [['100', '100', '100', '100', '100', '100'], 
                   ['200', '200', '200', '200', '200', '200'], 
                   ['300', '300', '300', '300', '300', '300'], 
                   ['400', '400', '400', '---', '400', '400'], 
                   ['500', '---', '500', '---', '500', '500']]


# C.4.
def test_print_game_table(capsys):
  # Examples from spec
  simple_data = {'CAT_A': {'100': ('Q', 'A'), '300': ('Q', 'A')},
                 'CAT_B': {'100': ('Q', 'A'), '200': ('Q', 'A'), '300': ('Q', 'A')}}
  test_ret = print_game_table(simple_data)
  assert not test_ret # nothing should be returned
  test_out = capsys.readouterr().out
  # If this test fails, double-check spacing at end of lines 
  assert test_out == """CAT_A | CAT_B
-------------
100   | 100  
---   | 200  
300   | 300  
---   | ---  
---   | ---  
"""

  # Testing example game data next
  game_data = example_game_data[2]
  print_game_table(game_data) # example imported same as C.2. 
  test_out = capsys.readouterr().out

  # If this test fails, double-check spacing at end of lines 
  assert test_out == """GEOGRAPHY | BY THE NUMBERS | TOYS & GAMES | TRANSPORTATION | FLOWERS & TREES | TRIVIA
-------------------------------------------------------------------------------------
100       | 100            | 100          | 100            | 100             | 100   
200       | 200            | 200          | 200            | 200             | 200   
300       | 300            | 300          | ---            | ---             | 300   
400       | 400            | 400          | ---            | ---             | 400   
500       | 500            | 500          | 500            | ---             | 500   
"""


# C.5.
def test_play_round(capsys):
  # Testing with example game data and some example run-throughs from spec
  game_data = example_game_data[2]
  # Example 1: same-casing for category, correct answer
  input_values = ['By the Numbers', '100', 'twenty questions']

  # override user input, capture values
  def mock_input(s):
    print(s)
    next_input = input_values[0]
    del input_values[0]
    return next_input

  # override input function to catch it
  midterm_partC.input = mock_input

  # Round 1!
  test_ret = play_round(game_data)
  assert test_ret == 100 # value for that round should be returned if correct
  test_out = capsys.readouterr().out
  out_lines = test_out.splitlines()
  assert '\n'.join(out_lines[:7]) == \
"""GEOGRAPHY | BY THE NUMBERS | TOYS & GAMES | TRANSPORTATION | FLOWERS & TREES | TRIVIA
-------------------------------------------------------------------------------------
100       | 100            | 100          | 100            | 100             | 100   
200       | 200            | 200          | 200            | 200             | 200   
300       | 300            | 300          | ---            | ---             | 300   
400       | 400            | 400          | ---            | ---             | 400   
500       | 500            | 500          | 500            | ---             | 500   """
  out_lines = out_lines[7:]
  # After table is displayed, check that prompts are correct
  assert out_lines[0] == 'Choose a category: '
  assert out_lines[1] == 'Choose a value: '
  assert out_lines[2].replace(':', '') == '(Q) The 1st asked in this game is usually "Animal, vegetable or mineral?"'
  assert out_lines[3].replace(':', '') == '(A) What is '
  # Make sure to count twenty questions as correct
  # ignores case with 'Twenty Questions'
  assert out_lines[4] == 'Correct!'

  # Round 2! Unfortunately, liberty bell doesn't match The Liberty Bell answer.
  # Feature request: Levenshtein distance!
  input_values = ['trivia', '200', 'liberty bell']
  test_ret = play_round(game_data)
  assert test_ret == 0 # incorrect...
  test_out = capsys.readouterr().out
  out_lines = test_out.splitlines()
  assert '\n'.join(out_lines[:7]) == \
"""GEOGRAPHY | BY THE NUMBERS | TOYS & GAMES | TRANSPORTATION | FLOWERS & TREES | TRIVIA
-------------------------------------------------------------------------------------
100       | ---            | 100          | 100            | 100             | 100   
200       | 200            | 200          | 200            | 200             | 200   
300       | 300            | 300          | ---            | ---             | 300   
400       | 400            | 400          | ---            | ---             | 400   
500       | 500            | 500          | 500            | ---             | 500   """
  out_lines = out_lines[7:]
  assert out_lines[0] == 'Choose a category: '
  assert out_lines[1] == 'Choose a value: '
  # leniency with : character in all prompts
  assert out_lines[2].replace(':', '') == '(Q) When it was rung for Chief Justice John Marshall\'s funeral, it cracked'
  assert out_lines[3].replace(':', '') == '(A) What is '
  assert out_lines[4] == 'Incorrect.'
  # Don't forget to print out the correct answer in shown format from spec
  assert out_lines[5].replace(':', '') == '(Correct answer) What is the Liberty Bell'

  # Test third round, no input ('') for answer (should be taken as incorrect)
  # Reset user input values
  input_values = ['geography', '500', ''] 
  test_ret = play_round(game_data)
  test_out = capsys.readouterr().out
  out_lines = test_out.splitlines()
  assert '\n'.join(out_lines[:7]) == \
"""GEOGRAPHY | BY THE NUMBERS | TOYS & GAMES | TRANSPORTATION | FLOWERS & TREES | TRIVIA
-------------------------------------------------------------------------------------
100       | ---            | 100          | 100            | 100             | 100   
200       | 200            | 200          | 200            | 200             | ---   
300       | 300            | 300          | ---            | ---             | 300   
400       | 400            | 400          | ---            | ---             | 400   
500       | 500            | 500          | 500            | ---             | 500   """
  out_lines = out_lines[7:] # we only care about prompts now
  assert out_lines[0] == 'Choose a category: '
  assert out_lines[1] == 'Choose a value: '
  assert out_lines[2].replace(':', '') == '(Q) Clocks in Lima, Peru, read the same as in this U.S. time zone'
  assert out_lines[3].replace(':', '') == '(A) What is '
  assert out_lines[4] == 'Incorrect.'
  assert out_lines[5].replace(':', '') == '(Correct answer) What is Eastern'

  # Round 4 test to check for earnings > 100
  # Reset input values
  input_values = ['trivia', '500', 'the Olympic Torch']
  test_ret = play_round(game_data)
  test_out = capsys.readouterr().out
  # test for round earnings > 100
  assert test_ret == 500


# # C.6.
# def test_start_game():
#   pass


def test_requirements():
  """
  Does some basic checking for function calls that student's should
  not have in their solution, either explicitly told not to or 
  to help them identify cases when they might have too many calls.
  """
  with open('midterm_partC.py') as f:
    count_keys = 0
    # There shouldn't be any calls to read(), readlines(),
    # or dict.values()
    flags = ['read(', 'readlines(', 'values(', 'isinstance(', 
             'dummy_data', 'example_game_data', 'TODO']
    for line in f:
      for flag in flags:
        assert flag not in line
      if 'keys()' in line:
        count_keys += 1
      # There should only be one call to keys()
      # in print_game_table
      # Remember to use `if key in dict` or `for key in dict` syntax
      assert count_keys <= 1

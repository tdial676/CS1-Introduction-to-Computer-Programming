from midterm_partC import * 
from midterm_partB import *
example_game_data ={
'GEOGRAPHY': 
     {'100': ('Christmas, Easter, or Bermuda, for example', 'islands'), 
      '200': ('Europe\'s only wild monkeys live on this "rock"', '(rock of) Gibraltar'), 
      '300': ('1/3 the size of U.S., this royal kingdom has no rivers or lakes but lots of oil', 'Saudi Arabia'), 
      '400': ('Largest country entirely in Europe', 'France'), 
      '500': ('Clocks in Lima, Peru, read the same as in this U.S. time zone', 'Eastern')},
  'BY THE NUMBERS': 
      {'100': ('The 1st asked in this game is usually "Animal, vegetable or mineral?"', 'Twenty Questions'), 
       '200': ('The two point values an ace can have in blackjack', '1 and 11'), 
       '300': ('Police precinct Barney Miller "dozen" work at any more', 'the 12th'), 
       '400': ('A race run by couples tied together at the ankle', 'a 3-legged race'), 
       '500': ('Musical about Continental Congress, it included song "Sit Down, John"', '1776')}

} 
fn_name = 'dice'
args = {'n': ('int', ''),
        'm': ('int', 'Number of sides per dice (>= 1)')}
ret_data = ('int', '')
fn_desc = 'Simulates `n` randomly-rolled `m`-sided dice, returning the sum of all rolls.'
print_fn_stub(fn_name, args, ret_data, fn_desc)


  
  
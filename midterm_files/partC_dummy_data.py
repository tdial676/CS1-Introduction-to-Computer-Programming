example_game_data = ('1984-09-13', 25, 
  {'GEOGRAPHY': 
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
       '500': ('Musical about Continental Congress, it included song "Sit Down, John"', '1776')}, 
  'TOYS & GAMES': 
      {'100': ('Number of pockets on a pool table', '6'), 
       '200': ('Color that always has opening move in chess', 'white'), 
       '300': ('Versions of this board game take place in London, Madrid, & Atlantic City', 'Monopoly'), 
       '400': ('Binney & Smith makes them in 64 colors', '(Crayola) crayons'), 
       '500': ("She's been a teenage fashion model for over 25 years", 'Barbie')}, 
  'TRANSPORTATION': 
      {'100': ('It could be paddle wheel, cargo or tramp', 'a steamer'), 
       '200': ('Charlton Heston was "on track" with it in "Ben Hur"', 'a chariot'), 
       '500': ('Vehicle Butch Cassidy rode during <a href="http://www.j-archive.com/media/1984-09-20_J_21.mp3">this</a> song:', 'a bicycle')}, 
  'FLOWERS & TREES': 
      {'100': ('Its seed is used in baking, but 1 type produces opium', 'the poppy'), 
       '200': ('Long associated with Lebanon, this tree is on its flag', 'a cedar')}, 
  'TRIVIA': 
      {'100': ('In 1983 Americans used over 1 million gallons of this beach product', 'suntan lotion'), 
       '200': ("When it was rung for Chief Justice John Marshall's funeral, it cracked", 'the Liberty Bell'), 
       '300': ('"Kingdom" that Khrushchev couldn\'t visit in 1959 U.S. trip', 'the Magic Kingdom/Disneyland'), 
       '400': ('Dr. Seuss\' egg-hatching elephant who was "faithful, 100%"', 'Horton'), 
       '500': ('It spent the night in a discount-house parking lot before heading to L.A. Coliseum', 'the Olympic torch')}
  }
)

def dict_to_table(dict, int_num):
  """
  """
  final_lst = []
  for num in range(int_num):
    new_lst = []
    value = str((num + 1) * 100)
    for nums in range(len(dict)):
      catagory = dict[list(dict.keys())[nums]]
      score = list(catagory.keys())[nums]
      if score != value:
        new_lst.append('---')
      else:
        new_lst.append(value)
    final_lst.append(new_lst)
  return final_lst
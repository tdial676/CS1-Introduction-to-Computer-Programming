"""
Thierno Diallo

Lab4b

This file contains numerous functions for accessing and altering 
our pokemon index and our collected number of pokemon, such as renaming,
adding, and removing pokemon and more. 
"""

import csv
import random
from os.path import exists
from lab4a import load_data, clear_data


"""
Provided starter code for program constants (students don't need to use these;
they are provided for starter/game functions). DO NOT ADD ANY GLOBAL VARIABLES
OR FLOATING PRINT/FUNCTION CALLS TO THIS FILE.
"""
COLLECTED_COLUMNS = ['id', 'name', 'nickname', 'level', 
                     'type', 'weakness', 'hp'] 

LVL_COEFFICIENT = 1.1 # hp stats -> (lvl * 1.1) + base hp

STARTER_LVL = 5
MAX_LVL = 100


# B.1. Utility Functions
# B.1.a.
def filter_row(rows, col, value):
    """
    This function returns the first row containing a value in a given column.

    Arguments:
      - a list of dictionaires = rows
      - a str column name = col
      - a str value = value
    Return Value: a dictionary containing the first row with the value
    """
    for dic in rows:
      if col in dic:
          return dic
  

# B.1.b.
def get_nth_row(filename, n):
    """
    This function takes csv file name and an int and returns the 
    nth row.

    Argument: 
      - a str csv file name 
      - an int n that represents a row in the csv file thus n needs to be
       between 1 and the number of rows in the file.

    Return Value: 
      the nth row as a dictionary if n is valid, and
      if n is invalid the function will return None.
    """
    with open(filename, 'r') as csv_file:
        reader = list(csv.DictReader(csv_file))
        if n > (len(reader)) or n < 1:
            return None
        else:
            return reader[n - 1]


# B.1.c.
def update_row(filename, line_num, rows, column, value):
  """
  This function replaces the value of a given column in a line in a file  
  with a given value and returns a bool corresponding to whether the value 
  was replaced.

  Arguments:
    - a str csv file name
    - an int line number
    - a list of dictionaires as rows
    - a str column name
    - a str new value 
  Return Value: a bool, True if the value was replaced or False if it was not 
  """
  if line_num < 1 or line_num > len(rows):
    print('Invalid entry given.')
    return False
  else:
    rows[line_num - 1][column] = value
    with open(filename, 'w', newline='') as csv_file:
      #keys are id,name,nickname,level,type,weakness,hp
      writer = csv.DictWriter(csv_file, fieldnames = rows[0].keys())
      writer.writeheader()
      for dic in rows:
        writer.writerow(dic)
    return True


# B.2.a.
def load_pokedex():
  """
  This function returns the pokimon index as a list of dictionaries
  
  Arguments: None
  Return Value: a list of dictionaries
  """
  return load_data('pokedex.csv')


# B.2.b.
def load_collected():
  """
  This function returns the collected pokemon index as a 
  list of dictionaries
  
  Arguments: None
  Return Value: a list of dictionaries
  """
  return load_data('collected.csv')


# B.3.a.
def display_pokedex(pokedex):
  """
  This function takes the pokidex prints the name, id, and type of each
  pokemon on it's own line.

  Argument: the pokidex as list of dictionaries
  Return Value: None
  """
  print('-' * 30)
  print('Full Pokedex Information:')
  print('-' * 30)
  for pokemon in pokedex:
    name = pokemon['name']
    id = pokemon['id']
    type = pokemon['type']
    print(f'#{id}: {name} ({type})')


# B.3.b.
def display_collected():
  """
  This function prints the pokemon in the collected pokemon 
  index (one pokemon per line).

  Argument: None
  Return Value: None
  """
  if not exists('collected.csv'):
    print('No Pokemon collected yet.')
  else:
    print('-' * 30)
    print('Your collected Pokemon:')
    print('-' * 30)
    with open('collected.csv', 'r') as csv_file:
      collected = list(csv.DictReader(csv_file))
      for pokemon in collected:
        name = pokemon['name']
        id = collected.index(pokemon) + 1
        type = pokemon['type']
        nickname = pokemon['nickname']
        print(f'{id}: {name} "{nickname}" ({type})')
  

# B.4. Adding Pokemon to Collected
def add_pokemon(pokemon):
  """
  This function takes a pokemon dictionary containging its info and 
  adds that info to the collected pokemon index. The user is also
  prompted to give their new pokemon a nickname if they want to.

  Argument: a dictionary for a pokemon
  Return Value: None
  """
  name = pokemon['name']
  nickname = ''
  prompt = input(f'Do you want to give a name to your new {name} ' + \
                 '(y for yes)? ')
  if prompt.lower() == 'y':
    while not nickname:
      nickname = input('What nickname do you want to give? ')
  else:
    nickname = name.upper() # default to UPPERCASE name
  pokemon['nickname'] = nickname
  #level = pokemon['level'] #old
  level = STARTER_LVL
  if 'level' in pokemon:
    level = pokemon['level']
  with open('collected.csv', 'a', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = COLLECTED_COLUMNS)
    writer.writerow({
                    'id': pokemon['id'], 'name': name, 'nickname': nickname,
                    'level': level, 'type': pokemon['type'],
                    'weakness': pokemon['weakness'], 'hp': pokemon['hp']
                     })


# B.5. Removing Pokemon from collected.csv
def abandon_pokemon():
  """
  Prompts the user to choose a Pokemon they want to say goodbye to
  (removing it from their collected.csv Pokemon). A user cannot
  abandon their only Pokemon if they have only one left.
  """
  display_collected()
  cid = input('Which Pokemon do you want to say goodbye to (Enter #)? ')
  # cid resents 'collected' pokemon id (determined by row number)
  cid = int(cid) 
  collected = load_collected()
  if cid < 1 or cid > len(collected):
    print('Invalid entry given')
  elif len(collected) == 1:
    print('You\'re abandoning your only Pokemon!\n' +
    'You will have to reset your collected Pokemon in ' +
    'the main menu if you want to do so.')
  else:
    del collected[cid - 1]
    with open('collected.csv', 'w', newline='') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames = collected[0].keys())
      writer.writeheader()
      writer.writerows(collected)


# B.6. Renaming
def rename_pokemon(cid, new_name):
  """
  Renames a Pokemon using the given collected id to the given
  new_name string.
  """
  collected = load_data('collected.csv')
  old_name = collected[cid - 1]['nickname']
  if update_row('collected.csv', cid, collected, 'nickname', new_name):
    print(f'Successfully renamed {old_name} to {new_name}')


# NOTE: You do not need to modify anything below for HW4 Part B.

# New Game Logic Stubs (Not Required for HW4)
def new_game(pokedex):
  pass


def populate_move_data(pokemon, pokedex):
  pass


def play(pokemon, opponent):
  pass


def choose_move(pokemon):
  pass


def play_move(move, pokemon, opponent):
  pass


def process_results(move_results, pokemon, opponent):
  pass


def process_win(pokemon, opponent):
  pass


def level_up(pokemon):
  pass


"""
Provided starter code for helper functions related to game logic.
"""
def generate_random_pokemon(pokedex):
  """
  Returns a randomly selected Pokemon dictionary from the given pokedex,
  filtering out columns needed for collected.csv.
  Argument:
    `pokedex` - list of Pokemon dictionaries in the Pokedex.
  """
  pokemon = random.choice(pokedex)
  name = pokemon['name']
  nickname = name.upper()
  info = [pokemon['id'], name, nickname, str(STARTER_LVL), 
          pokemon['type'], pokemon['weakness'], pokemon['hp']]
  pokemon = { k:v for k,v in zip(COLLECTED_COLUMNS, info)}
  return pokemon


def assign_starter(pokedex):
  """
  Randomly assigns a starter Pokemon from the given list of Pokemon
  dictionaries and adds it to the user's collected.csv dataset.
  The user has an option to give the Pokemon a nickname (defaulting)
  to the Pokemon's name in UPPERCASE if they don't want to.
  Argument:
    `pokedex` - list of Pokemon dictionaries in the Pokedex.
  """
  pokemon = generate_random_pokemon(pokedex)
  name = pokemon['name']
  print(f'Your new starter is {name}!')
  add_pokemon(pokemon)
  nickname = pokemon['nickname']
  print('Successfully restarted your collected Pokemon with ' + \
        f'your new starter {name} ("{nickname}")!')


"""
Provided starter code related to UI below.
"""
def show_options():
  """
  Displays a list of menu options for the user, prompts
  them to provide an option, and returns their input.
  Ignores letter-casing and extra whitespace in prompt choice.
  """
  print('What would you like to do?')
  print('  \'pokedex\' - View all Pokemon in the Pokedex')
  print('  \'collected\' - View all Pokemon you have collected')
  print('  \'add\' - Add a new Pokemon to your collection')
  print('  \'goodbye\' - Say goodbye to one of your collected Pokemon...')
  print('  \'reset\' - Reset your collected Pokemon with a new starter')
  print('  \'rename\' - Rename one of your collected Pokemon')
  print('  \'play\' - Start a new game')
  print('  \'q\' - Quit')
  print()
  option = input('Enter your option: ').lower().strip()
  print()
  return option


def prompt_add_pokemon(pokedex):
  """
  Prompts the user for a Pokedex ID to add a Pokemon to their collection.
  Note: This function is provided for students to quickly test their
  add_pokemon functionality without the gameplay implementation (in the 
  completed version, Pokemon can only be added after defeating them
  in a Pokemon battle).
  """
  display_pokedex(pokedex)
  pid = -1
  while True:
    pid = int(input('Which Pokemon do you want to collect (enter an ID #)? '))
    if pid < 1 or pid > len(pokedex):
      print('Invalid ID #')
      pid = int(input('Which Pokemon do you want to collect (enter an ID #)? '))
    else:
      pokemon = pokedex[pid - 1]
      add_pokemon(pokedex[pid - 1])
      print(f'Successfully added {pokemon["name"]} to collected!')
      break


def prompt_clear_collected():
  """
  Prompts the user to confirm erasing their collected Pokemon data.
  If confirmed, clears the rows (keeps the column headers).
  Return:
    boolean - True if the dataset was cleared, otherwise false.
  """
  confirm = input('Are you sure you want to erase all of your ' + \
                  ' collected data (y for yes)? ')
  if confirm.lower() == 'y':
    clear_data('collected.csv')
    return True
  else:
    print('Aborting.')
    return False


def prompt_rename_pokemon():
  """
  Displays the user's currently-collected Pokemon to choose from, and
  prompts the user to select one to rename. If given a valid entry number
  for the collected Pokemon (corresponding to the numbers listed), renames
  the chosen Pokemon in the collected dataset.
  """
  display_collected()
  cid = input('Which Pokemon would you like to rename? ')
  new_name = input('What is the new name you\'d like to give this Pokemon? ')
  rename_pokemon(int(cid), new_name)


def start_ui(pokedex):
  """
  Displays the main menu options to the user and prompts
  them for an option listed (reprompting until a valid one is provided).
  """
  option = show_options()
  options = { 'pokedex' : display_pokedex,
              'collected' : display_collected,
              'add' : prompt_add_pokemon,
              'reset' : prompt_clear_collected,
              'goodbye' : abandon_pokemon,
              'rename' : prompt_rename_pokemon,
              'play' : new_game,
              'q' : quit_game
            }
  while option not in options:
    print('Invalid option. Please enter an option listed.')
    option = show_options()
  if option == 'pokedex':
    display_pokedex(pokedex)
  elif option == 'add':
    prompt_add_pokemon(pokedex)
  elif option == 'play':
    # new_game(pokedex)
    print('Not yet implemented.')
  elif option == 'reset':
    if prompt_clear_collected():
      assign_starter(pokedex)
  else:
    options[option]()

  print() 
  reprompt = input('Do you want to do something else (y for yes)? ')
  if (reprompt.lower().startswith('y')):
    start_ui(pokedex)
  else:
    quit_game()


def quit_game():
  """
  Prints a good bye message and exits the program.
  """
  print('Good bye!')
  quit()


def main():
  """
  Starts the main menu for the Pokemon simulator, prompting the user
  to select a displayed option. Also initializes a collected.csv dataset
  if there isn't one that yet exists for the user.
  """
  print('Welcome to the Pokemon Battle Simulator!')
  pokedex = load_pokedex()
  if not exists('collected.csv'):
    # Write a single column header for the dataset.
    with open('collected.csv', 'w') as f:
      f.write(','.join(COLLECTED_COLUMNS) + '\n')
    # Assing a random Pokemon for the user's starter Pokemon.
    assign_starter(pokedex)
  # Start UI prompts.
  start_ui(pokedex)


if __name__ == '__main__':
  main()
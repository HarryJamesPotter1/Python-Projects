from typing import Optional, List
import random


rock_art = """
  -------
 -       -
|         |
|         |
 _       _
  -------
"""

paper_art = """
|---------|
|         |
|         |
|         |
|         |
|         |
|---------|
"""

scissors_art = """
  ---
|     |              ##
  ---  ##          ##
         ##     ##
            ###
          ##  ##
  ---  ##       ##
|     |           ##
  ---               ##
"""

choices = ["Rock","Paper","Scissors"]
#rock = 0, paper = 1, scissors = 2
choice_art = [rock_art,paper_art,scissors_art]

def build_valid_input_list(inputs: List[str]) -> str:
  """Builds a printable listing of valid inputs"""

  return ', '.join([f'{s[0]}[{s[1:]}]' for s in inputs])

def display_choice(choice_ind: int,chooser: str)-> None:
  """Displays a choice made from one of the choices.

  :param choice_ind: The index of choice to display.
  :param chooser: The name of the chooser
  
  """
  print(chooser, "chose", choices[choice_ind])
  print(choice_art[choice_ind])

#display_choice(0,"User")
#display_choice(1,"User")
#display_choice(2,"Computer")

def get_result(choice1: int, choice2: int):
    """
    Calculates the result of a game with the given choices.
    :return: 0 for a tie, 1 if `choice1` wins, 2 if `choice2` wins.
    """
    # A tie
    if choice1 == choice2:
        return 0
    # Choice 1 wins
    elif choice1 == ((choice2 + 1) % len(choices)):
        return 1
    # Choice 2 wins
    else:
        return 2

def index_from_input(inp: str) -> Optional[int]:
  """Gets the choice index from input.
  
  :return: The index if valid, None if invalid, -1 quit
  """

  if inp == 'q':
    return -1

  for i,choice in enumerate(choices):

    if choice.startswith(inp):
      return i
    

  return None
  
#print(index_from_input('Q') == -1)
#print(index_from_input('Rock') == 0)
#print(index_from_input('Paper') == 1)
#print(index_from_input('Scissors') == 2)

def get_player_input() -> int:
    """Returns the index of the player's choice, or -1 on quit"""

    inp_list = build_valid_input_list(choices)

    while True:
      inp = input(f'Enter one of {inp_list} or q to quit: ')
      ind = index_from_input(inp)
      if ind is None:
        print("Invalid choice, try again")
      
      else:
        return ind
      
Wins = 0
Losses = 0
Ties = 0

while True:

  player_choice = get_player_input()

  if player_choice < 0:
    break
  
  computer_choice = random.randrange(0, len(choices))
  display_choice(player_choice, 'Player')
  display_choice(computer_choice, 'Computer')

  result = get_result(player_choice,computer_choice)

  if result == 0:
    print("It is a tie!")
    Ties += 1
    print("Ties:", Ties)
    print("Wins:", Wins)
    print("Losses:", Losses)

  elif result == 1:
    print("You won")
    Wins += 1
    print("Wins:", Wins)
    print("Losses:", Losses)
    print("Ties:", Ties)

  else:
    print("You Lost")
    Losses += 1
    print("Losses:", Losses)
    print("Wins:", Wins)
    print("Ties:", Ties)


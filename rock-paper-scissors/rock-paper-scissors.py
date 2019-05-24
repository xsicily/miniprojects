#!/bin/python3

import random
from enum import Enum

class Weapon(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

player_choice = 'Rock'

game_round = 0

def weapon_count(player_choice):
    num_of_rock = 0
    num_of_paper = 0
    num_of_scissors = 0
    if Weapon[player_choice] == Weapon.Rock:
        num_of_rock = num_of_rock + 1
        return num_of_rock
    elif Weapon[player_choice] == Weapon.Paper:
        num_of_paper = num_of_paper + 1
        return num_of_paper
    else:
        num_of_scissors = num_of_scissors + 1
        return num_of_scissors

comp_choice = random.choice(list(Weapon))

if comp_choice == Weapon[player_choice]:
    game_round = game_round + 1
    print('Player and Computer tie' + ' ' + game_round + ' ' + 'round')
elif 






#!/bin/python3

import random

"""
def name_to_number(player_choice):
    if player_choice == 'r':
        num_of_rock = num_of_rock + 1
        weapon_choice_player[0] = num_of_rock
        return 0, weapon_choice_player
    elif player_choice == 'p':
        num_of_paper = num_of_paper + 1
        weapon_choice_player[1] = num_of_paper
        return 1, num_of_paper
    elif player_choice == 's':
        num_of_scissors = num_of_scissors + 1
        weapon_choice_player[2] = num_of_scissors
        return 2, num_of_scissors
    else:
        return 'Invalid entry! Please try it again!'
"""

def game_compare(comp_number, player_number):
    tie_round = 0
    comp_win_round = 0
    player_win_round = 0
    number_diff = comp_number - player_number
    if number_diff == 0:
        tie_round = tie_round + 1
        return tie_round, 'Game tie!'
    elif number_diff == -1 or number_diff == 2:
        player_win_round = player_win_round + 1
        return player_win_round, 'Player wins!'
    else:
        comp_win_round = comp_win_round + 1
        return comp_win_round, 'Computer wins!'


def rps(raw_input):
    """
    
    """
    q = True
    choice_of_player = {}
    game_round = 0
    num_of_rock = 0
    num_of_paper = 0
    num_of_scissors = 0
    while q == False:
        if raw_input == 'r':
            player_number = 0
            num_of_rock = num_of_rock + 1
            choice_of_player[0] = num_of_rock
        elif raw_input == 'p':
            player_number = 1
            num_of_paper = num_of_paper + 1
            choice_of_player[1] = num_of_paper
        elif raw_input == 's':
            player_number = 2
            num_of_scissors = num_of_scissors + 1
            choice_of_player[2] = num_of_scissors       
        else:
            print('Invalid entry! Please try it again!')

        game_round = game_round + 1

        if game_round < 2:
            comp_number = random.randrange(3)
            game_result = game_compare(comp_number, player_number)
        else:
            if player_number < 2:
                comp_number = player_number + 1
            else:
                comp_number = player_number - 2
            game_result = game_compare(comp_number, player_number)
        print(game_result[1])
        print("Do you want to play again? (Y/N)") 
        ans = input() 
        game_status = []
        if ans == 'n' or ans == 'N':
            game_status = ['Player and Computer tie' + ' ' + game_result[0] + ' ' + 'round', 
            'Computer wins' + ' ' + game_result[1] + ' ' + 'round',
            'Player wins' + ' ' + game_result[2] + ' ' + 'round',
            'The number times the player selected Rock', choice_of_player[0],
            'The number times the player selected Paper', choice_of_player[1],
            'The number times the player selected Sciccors', choice_of_player[2]]
            return game_status
        break

if __name__ == "__main__":
    raw_input = 'r'
    rps(raw_input)


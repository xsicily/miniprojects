#!/bin/python3

import random
import operator

num_of_rock = 0
num_of_paper = 0
num_of_scissors = 0
r_dict = {}
p_dict = {}
s_dict = {}
choice_of_player = {}

def player_status(raw_input):
    """
    Input - string of raw_input
    Ouput - int of player_number: 
                            r or R - 0
                            p or P - 1
                            s or S - 2
            dictionary of choice_of_player:
                            key - 0, value - how many times the player selected Rock
                            key - 1, value - how many times the player selected Paper
                            key - 2, value - how many times the player selected Scissors
    >>> player_status('r')
    (0, {0: 1})
    >>> player_status('p')
    (1, {0: 1, 1: 1})
    """
    global num_of_rock, num_of_paper, num_of_scissors
    if raw_input == 'r' or raw_input == 'R':
        player_number = 0
        num_of_rock = num_of_rock + 1
        r_dict[0] = num_of_rock
    elif raw_input == 'p' or raw_input == 'P':
        player_number = 1
        num_of_paper = num_of_paper + 1
        p_dict[1] = num_of_paper
    elif raw_input == 's' or raw_input == 'S':
        player_number = 2
        num_of_scissors = num_of_scissors + 1 
        s_dict[2] = num_of_scissors
    elif raw_input == 'q' or raw_input == 'Q':
        player_number = 3
    else:
        print('Invalid entry! Please try it again!') 
    choice_of_player.update(r_dict)
    choice_of_player.update(p_dict)
    choice_of_player.update(s_dict)
    preferred_weapon = max(choice_of_player.items(), key=operator.itemgetter(1))[0]
    return player_number, choice_of_player, preferred_weapon

tie_round = 0
comp_win_round = 0
player_win_round = 0
tie_dict = {}
comp_win_dict = {}
player_win_dict = {}
game_result = {}

def game_compare(comp_number, player_number):
    """
    Input - int: computer number corresponding to the weapon choice
            int: player number corresponding to the weapon choice
    Output - how many rounds of game tie
             how many rounds player wins
             how many rounds computer wins
             string game status: tie, player wins or computer wins?
    """
    global tie_round, comp_win_round, player_win_round
    number_diff = comp_number - player_number
    if number_diff == 0:
        tie_round = tie_round + 1
        tie_dict['tie'] = tie_round
    elif number_diff == -1 or number_diff == 2:
        player_win_round = player_win_round + 1
        player_win_dict['player_win'] = player_win_round
    else:
        comp_win_round = comp_win_round + 1
        comp_win_dict['comp_win'] = comp_win_round
    game_result.update(tie_dict)
    game_result.update(player_win_dict)
    game_result.update(comp_win_dict)
    return game_result

def rps(raw_input):
    """
    Input - string raw_input
    Output - game status report
    """
    play = False
    while play == True:
        tup = player_status(raw_input)
        player_number = tup[0]
        choice_of_player = tup[1]
        preferred_weapon = tup[2]
        if player_number != 3:
            if len(choice_of_player) == 2 and len(set(choice_of_player.values())) == 1:
                comp_number = random.randrange(3)
            elif len(choice_of_player) == 3 and len(set(choice_of_player.values())) == 1:
                comp_number = random.randrange(3)
            else:
                if preferred_weapon == 2: 
                    comp_number = preferred_weapon - 2
                else:
                    comp_number = preferred_weapon + 1           
            game_result = game_compare(comp_number, player_number)
        else:
            print ('Player and Computer tie:' + ' ' + str(game_result['tie']) + ' ' + 'rounds')
            print ('Player wins:' + ' ' + game_result['player_win'] + ' ' + 'rounds')
            print ('Computer wins:' + ' ' + game_result['comp_win'] + ' ' + 'rounds')
            print ('The number times the player selected Rock:', choice_of_player[0])
            print ('The number times the player selected Paper:', choice_of_player[1])
            print ('The number times the player selected Sciccors:', choice_of_player[2])
            break
        break


if __name__ == "__main__":
    raw_input = 'r'
    rps(raw_input)
    raw_input = 'p'
    rps(raw_input)


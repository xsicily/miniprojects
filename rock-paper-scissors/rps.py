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

def player(raw_input):
    """
    Input - string of raw_input
    Ouput - int of player_number: 
                            r or R - 1
                            p or P - 2
                            s or S - 3
                            q or Q - 0
            dictionary of choice_of_player:
                            key - 0, value - how many times the player selected Rock
                            key - 1, value - how many times the player selected Paper
                            key - 2, value - how many times the player selected Scissors
    >>> player_status('r')
    (0, {1: 1})
    >>> player_status('p')
    (1, {1: 1, 2: 1})
    """
    global num_of_rock, num_of_paper, num_of_scissors
    if raw_input == 'r' or raw_input == 'R':
        player_number = 1
        num_of_rock = num_of_rock + 1
        r_dict[0] = num_of_rock
    elif raw_input == 'p' or raw_input == 'P':
        player_number = 2
        num_of_paper = num_of_paper + 1
        p_dict[1] = num_of_paper
    elif raw_input == 's' or raw_input == 'S':
        player_number = 3
        num_of_scissors = num_of_scissors + 1 
        s_dict[2] = num_of_scissors
    elif raw_input == 'q' or raw_input == 'Q':
        player_number = 0
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
game_round = 0


def rps(raw_input):
    """
    Input - string raw_input
    Output - game status report
    """
    global tie_round, comp_win_round, player_win_round, game_round
    play = True
    while play:
        game_round = game_round + 1
        tup = player(raw_input)
        player_number = tup[0]
        choice_of_player = tup[1]
        preferred_weapon = tup[2]
        if player_number == 0:
            show_results()
            break
        else: 
            if len(choice_of_player) == 2 and len(set(choice_of_player.values())) == 1:
                comp_number = random.randrange(3)
            elif len(choice_of_player) == 3 and len(set(choice_of_player.values())) == 1:
                comp_number = random.randrange(3)
            else:
                if preferred_weapon == 3: 
                    comp_number = preferred_weapon - 2
                else:
                    comp_number = preferred_weapon + 1           
            number_diff = comp_number - player_number
            if number_diff == 0:
                tie_round = tie_round + 1
                print('Game tie!')
            elif number_diff == -1 or number_diff == 2:
                player_win_round = player_win_round + 1
                print('You win!')
            else:
                comp_win_round = comp_win_round + 1
                print('Computer wins!')


def show_results():
    print ('Player and Computer tie:' + ' ' + tie_round + ' ' + 'rounds')
    print ('Player wins:' + ' ' + player_win_round + ' ' + 'rounds')
    print ('Computer wins:' + ' ' + comp_win_round + ' ' + 'rounds')
    print ('The number times the player selected Rock:', choice_of_player[0])
    print ('The number times the player selected Paper:', choice_of_player[1])
    print ('The number times the player selected Sciccors:', choice_of_player[2])

if __name__ == "__main__":
    raw_input = 'r'
    rps(raw_input)
    raw_input = 'p'
    rps(raw_input)


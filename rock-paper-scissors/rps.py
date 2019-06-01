#!/bin/python3

import random
import operator

num_of_rock = 0
num_of_paper = 0
num_of_scissors = 0
choice_of_player = {}

def user(raw_input):
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
    """
    global num_of_rock, num_of_paper, num_of_scissors, player_number
    if raw_input == 'r' or raw_input == 'R':
        player_number = 1
        choice_of_player[1] = num_of_rock
        choice_of_player[2] = num_of_paper
        choice_of_player[3] = num_of_scissors
        num_of_rock = num_of_rock + 1
    elif raw_input == 'p' or raw_input == 'P':
        player_number = 2
        choice_of_player[1] = num_of_rock
        choice_of_player[2] = num_of_paper
        choice_of_player[3] = num_of_scissors
        num_of_paper = num_of_paper + 1
    elif raw_input == 's' or raw_input == 'S':
        player_number = 3
        choice_of_player[1] = num_of_rock
        choice_of_player[2] = num_of_paper
        choice_of_player[3] = num_of_scissors
        num_of_scissors = num_of_scissors + 1 
    elif raw_input == 'q' or raw_input == 'Q':
        player_number = 0
        choice_of_player[1] = num_of_rock
        choice_of_player[2] = num_of_paper
        choice_of_player[3] = num_of_scissors
    else:
        return 'Invalid entry! Please try it again!'
    # make dictionary including all the weapon choice the player selected
    return player_number, choice_of_player


def computer(weapons_choice_of_user):
    """
    Input - dictionary of weapons choice including Rock, Paper and Scissors
    Output - according to user's preferred weapon, to select the suitable weapon to beat user
    """
    global comp_number
    # check if player has preferred choice of weapon
    if weapons_choice_of_user[1] > weapons_choice_of_user[2] and weapons_choice_of_user[1] > weapons_choice_of_user[3]:
        preferred_weapon = True
    elif weapons_choice_of_user[2] > weapons_choice_of_user[1] and weapons_choice_of_user[2] > weapons_choice_of_user[3]:
        preferred_weapon = True
    elif weapons_choice_of_user[3] > weapons_choice_of_user[1] and weapons_choice_of_user[3] > weapons_choice_of_user[2]:
        preferred_weapon = True
    else:
        preferred_weapon = False
    # choose weapons based on preferred weapons from user
    if True == preferred_weapon:
        user_preferred_weapon = max(weapons_choice_of_user.items(), key=operator.itemgetter(1))[0]
        if user_preferred_weapon == 3: 
            comp_number = user_preferred_weapon - 2
        else:
            comp_number = user_preferred_weapon + 1 
    else:
        comp_number = random.randrange(3) + 1                    
    return comp_number

tie_round = 0
comp_win_round = 0
user_win_round = 0
game_round = 0


def rps(user_status):
    """
    Input - user_status including user_number and dictionary of weapons_choice_of_user
    Output - game status report
    """
    global tie_round, comp_win_round, user_win_round, game_round
    user_number = user_status[0]
    weapons_choice_of_user = user_status[1]
    comp_number = computer(weapons_choice_of_user)
    if user_number != 0:
        game_round = game_round + 1
        number_diff = comp_number - user_number
        if number_diff == 0:
            tie_round = tie_round + 1
            return "Game tie!"
        elif number_diff == -1 or number_diff == 2:
            user_win_round = user_win_round + 1
            return 'User win!'
        else:
            comp_win_round = comp_win_round + 1
            return 'Computer wins!'
    else:
        return 'Total games:' + ' ' + str(game_round) + ' ' + 'rounds', \
               'Game tie:' + ' ' + str(tie_round) + ' ' + 'rounds', \
               'Player wins:' + ' ' + str(user_win_round) + ' ' + 'rounds', \
               'Computer wins:' + ' ' + str(comp_win_round) + ' ' + 'rounds', \
               'The player selected Rock:' + ' ' + str(weapons_choice_of_user[1]) + ' ' + 'times', \
               'The player selected Paper:' + ' ' + str(weapons_choice_of_user[2]) + ' ' + 'times', \
               'The player selected Sciccors:' + ' ' + str(weapons_choice_of_user[3]) + ' ' + 'times' 


def main():
    raw_input = 'r'
    user_status = user(raw_input)
    rps(user_status)
    raw_input = 'r'
    user_status = user(raw_input)
    rps(user_status)
    raw_input = 's'
    user_status = user(raw_input)
    rps(user_status)
    raw_input = 'q'
    user_status = user(raw_input)
    game_result = rps(user_status)
    return game_result

if __name__ == "__main__":
    print(main())






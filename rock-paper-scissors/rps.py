#!/bin/python3

import random
import operator
import player

tie_round = 0
comp_win_round = 0
user_win_round = 0
game_round = 0


def rps(player_number, comp_number):
    """
    Input - string raw_input
    Output - game status report
    """
    global tie_round, comp_win_round, user_win_round, game_round
    play_quit = True
    while not play_quit:
        game_round = game_round + 1
        if user_number != 0:
            number_diff = comp_number - user_number
            if number_diff == 0:
                tie_round = tie_round + 1
                return 'Game tie!'
            elif number_diff == -1 or number_diff == 2:
                user_win_round = user_win_round + 1
                return 'User win!'
            else:
                comp_win_round = comp_win_round + 1
                return 'Computer wins!'
        else:
            play_quit = True
            return 'Game Over!'


            show_results()
            print('Total games:' + ' ' + str(game_round) + ' ' + 'rounds')
            print ('Player and Computer tie:' + ' ' + str(tie_round) + ' ' + 'rounds')
            print ('Player wins:' + ' ' + str(user_win_round) + ' ' + 'rounds')
            print ('Computer wins:' + ' ' + str(comp_win_round) + ' ' + 'rounds')
            print ('The number times the player selected Rock:', weapon_records_of_user[1])
            print ('The number times the player selected Paper:', weapon_records_of_user[2])
            print ('The number times the player selected Sciccors:', weapon_records_of_user[3])


if __name__ == "__main__":
    raw_input = 'q'
    user_status = player.user(raw_input)
    user_number = user_status[0]
    weapon_records_of_user = user_status[1]
    comp_number = player.comp(user_status)
    rps(user_number, comp_number)


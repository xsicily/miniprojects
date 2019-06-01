#!/bin/python3

import random
from enum import Enum

class Choice(Enum):
    R = 1
    P = 2
    S = 3
    Q = 0

raw_input = 'R'

class Player():
    def __init__(self, player_choice, weapon_r_count, weapon_p_count, weapon_s_count, weapon_used_hist):
        self.player_choice = Choice[raw_input.upper()]
        self.weapon_r_count = 0
        self.weapon_p_count = 0
        self.weapon_s_count = 0
        self.weapon_used_hist = {}
    def get_weapon_info(self):
        player_choice = Choice[raw_input.upper()]
        if player_choice == Choice.R:
            self.weapon_used_hist[1] = self.weapon_r_count
            self.weapon_used_hist[2] = self.weapon_p_count
            self.weapon_used_hist[3] = self.weapon_s_count
            self.weapon_r_count += 1
        elif player_choice == Choice.P:
            self.weapon_used_hist[1] = self.weapon_r_count
            self.weapon_used_hist[2] = self.weapon_p_count
            self.weapon_used_hist[3] = self.weapon_s_count
            self.weapon_p_count += 1
        elif player_choice == Choice.S:
            self.weapon_used_hist[1] = self.weapon_r_count
            self.weapon_used_hist[2] = self.weapon_p_count
            self.weapon_used_hist[3] = self.weapon_s_count
            self.weapon_s_count += 1
        elif player_choice == Choice.Q:
            self.weapon_used_hist[1] = self.weapon_r_count
            self.weapon_used_hist[2] = self.weapon_p_count
            self.weapon_used_hist[3] = self.weapon_s_count      
        else:
            return 'Invalid entry! Please try it again!'
        return player_choice, self.weapon_used_hist

class Computer():
    def __init__(self, comp_choice):
        self.comp_choice = random.choice(list(Choice))







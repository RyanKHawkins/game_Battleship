# Title:  Battleship
# Author:  Ryan Hawkins
# Update:  2019-11-02

import os


def clear():
    os.system('cls' if os.name == 'nit' else 'clear')


def create_blank_board():
    board = {}
    EMPTY = " "

    for row in range(1, 11):
        for column in range(1, 11):
            board[(row, column)] = EMPTY
    return board


def set_pieces():
    pass


def create_player_board():
    player_board = create_blank_board()
    set_pieces(player_board)


def create_enemy_board():
    pass


def create_enemy_map():
    pass


def display_boards(player_board, enemy_map):
    pass

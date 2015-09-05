from gui.gui import *
from common.board import *
from common.state import *
from common.player import *


class Game():

    def __init__(self, board,first_player, second_player ):
        self.board = board
        self.first_player = first_player
        self.second_player = second_player
        self.current_player_colour = State.black
        
    def get_current_player(self):
        if self.first_player.colour == self.current_player_colour:
            return self.first_player

        return self.second_player

    def get_other_player(self):
        if self.first_player.colour == self.current_player_colour:
            return self.second_player

        return self.first_player

    def change_current_player(self):
        if self.current_player_colour == State.black:
            self.current_player_colour = State.white
        else:
            self.current_player_colour = State.black

    def is_game_won(self):
        valid_moves = self.board.get_valid_moves(self.current_player_colour)
        if len(valid_moves) == 0:
            return True
        return False

    def get_winner(self):
        if self.first_player.score > self.second_player.score:
            return self.first_player
        if self.second_player.score > self.first_player.score:
            return self.second_player

        return None

    def reset_game(self):
        self.board = self.board.reset()
        self.first_player.score = 2
        self.first_player.board = self.board
        self.second_player.board = self.board
        self.second_player.score = 2
        self.current_player_colour = State.black

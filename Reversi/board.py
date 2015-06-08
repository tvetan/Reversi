from piece import Piece
from state import State


class Board():

    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = [
            [Piece(x, y, State.empty) for y in range(self.width)]
            for x in range(self.height)
        ]

    def make_white(self, x, y):
        self.change_piece(x, y, State.white)

    def make_black(self, x, y):
        self.change_piece(x, y, State.black)

    def make_empty(self, x, y):
        self.change_piece(x, y, State.empty)

    def change_piece(self, x, y, state):
        self.pieces[x][y] = state

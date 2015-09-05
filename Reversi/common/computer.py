import random

from common.player import Player


class Computer(Player):

    def __init__(self, colour, board):
        super().__init__(colour, board)

    def easy_move(self):
        valid_moves = self.board.get_valid_moves(self.colour)
        move = None
        if valid_moves:
            random.shuffle(valid_moves)
            choice = random.choice(range(len(valid_moves)))
            move = valid_moves[choice]

            return move, self.board.is_valid_move(move[0], move[1], self.colour)

    def make_move(self, other_player):
        best_move = self.easy_move()
        x, y = best_move[0]
        tiles_to_flip = best_move[1]
        self.board.pieces[x][y].state = self.colour

        for sector in tiles_to_flip:
            self.board.pieces[sector[0]][sector[1]].state = self.colour

        self.score += 1 + len(tiles_to_flip)
        other_player.score -= len(tiles_to_flip)
        return True

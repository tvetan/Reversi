import random

from common.player import Player


class Computer(Player):

    def __init__(self, colour, board):
        super().__init__(colour, board)

    def easy_move(self):
        valid_moves = self.board.get_valid_moves()
        move = None
        if valid_moves:
            random.shuffle(valid_moves)
            choice = random.choice(range(len(valid_moves)))
            move = valid_moves[choice]

            return move, self.board.is_valid_move(move[0], move[1])

    def make_move(self, other_player):
        best_move = self.easy_move()
        x, y = best_move[0]
        tiles_to_flip = best_move[1]
        self.board.board[x][y] = self.colour

        for sector in tiles_to_flip:
            self.board.board[sector[0]][sector[1]] = self.colour

        self.score += 1 + len(tiles_to_flip)
        other_player.score -= len(tiles_to_flip)
        return True

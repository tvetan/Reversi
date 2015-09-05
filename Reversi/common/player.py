
HEIGHT = 8
WIDTH = 8
DIRECTIONS = ((0, 1), (1, 1), (1, 0), (1, -1),
              (0, -1), (-1, -1), (-1, 0), (-1, 1))

CORNERS = ((0, 0), (WIDTH-1, 0), (0, HEIGHT-1), (WIDTH-1, HEIGHT-1))


class Player():

    def __init__(self, colour, board):
        self.colour = colour
        self.board = board
        self.score = 2

    def make_move(self, mousex, mousey, other_player):
        tiles_to_flip = self.board.is_valid_move(mousex, mousey, self.colour)

        if not tiles_to_flip:
            return False

        self.board.pieces[mousex][mousey].state = self.colour
        for move in tiles_to_flip:
            self.board.pieces[move[0]][move[1]].state = self.colour

        self.score += 1 + len(tiles_to_flip)
        other_player.score -= len(tiles_to_flip)
        return True

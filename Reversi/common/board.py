from common.piece import Piece
from common.state import State

HEIGHT = 8
WIDTH = 8
DIRECTIONS = ((0, 1), (1, 1), (1, 0), (1, -1),
              (0, -1), (-1, -1), (-1, 0), (-1, 1))


class Board():

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.pieces = [
            [Piece(x, y, State.empty) for y in range(self.width)]
            for x in range(self.height)
        ]

        self.change_piece(int(WIDTH / 2) - 1, int(HEIGHT / 2) - 1, State.white)
        self.change_piece(int(WIDTH / 2) - 1, int(HEIGHT / 2), State.black)
        self.change_piece(int(WIDTH / 2), int(HEIGHT / 2) - 1, State.black)
        self.change_piece(int(WIDTH / 2), int(HEIGHT / 2), State.white)

    def make_white(self, x, y):
        self.change_piece(x, y, State.white)

    def make_black(self, x, y):
        self.change_piece(x, y, State.black)

    def make_empty(self, x, y):
        self.change_piece(x, y, State.empty)

    def change_piece(self, x, y, state):
        self.pieces[x][y].state = state

    def reset(self):
        self = Board()

        return self

    def is_inside(self, x, y):
        return x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT

    def is_valid_move(self, x, y, colour):
        if self.is_inside(x, y):
            if self.pieces[x][y].state != State.empty:
                return False
        else:
            return False

        self.pieces[x][y].state = colour
        other_colour = None
        if colour == State.white:
            other_colour = State.black
        else:
            other_colour = State.white

        tiles_to_flip = []

        for direction in DIRECTIONS:
            positionx, positiony = x, y
            positionx += direction[0]
            positiony += direction[1]

            while self.is_inside(positionx, positiony) and \
                    self.pieces[positionx][positiony].state == other_colour:
                positionx += direction[0]
                positiony += direction[1]

                if not self.is_inside(positionx, positiony):
                    continue

                if self.pieces[positionx][positiony].state == colour:
                    while True:
                        positionx -= direction[0]
                        positiony -= direction[1]

                        if positionx == x and positiony == y:
                            break
                        tiles_to_flip.append((positionx, positiony))

        self.pieces[x][y].state = State.empty

        if len(tiles_to_flip) > 0:
            return tiles_to_flip

        return False

    def get_valid_moves(self, colour):
        valid_moves = [(x, y) for x in range(0, WIDTH)
                       for y in range(0, HEIGHT)
                       if self.is_valid_move(x, y, colour)]

        return valid_moves

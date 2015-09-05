from gui.gui import *
from common.board import *
from common.game import *


def main():
    board = Board()
    gui = Gui(board)

    gui.show()

if __name__ == '__main__':
    main()

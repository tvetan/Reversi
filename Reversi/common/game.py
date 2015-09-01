from gui.gui import *
from common.board import *


class Game():

    def __init__(self, gui):
        self.board = Board()
        self.gui = gui

    def run(self):
        self.gui.show()

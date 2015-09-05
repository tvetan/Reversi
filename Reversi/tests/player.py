import unittest
from common.board import *
from common.state import State
from common.player import Player

class TestPlayer(unittest.TestCase):

    def test_initialize(self):
        board = Board()
        player = Player(State.white, board)

        self.assertEqual(player.colour, State.white)
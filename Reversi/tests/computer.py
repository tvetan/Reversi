import unittest

from common.computer import *
from common.state import *
from common.board import *


class TestComputer(unittest.TestCase):

    def test_initialize(self):
        board = Board()
        computer = Computer(State.white, board)

        self.assertEqual(computer.colour, State.white)
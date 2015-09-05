import unittest
from common.board import Board
from common.state import State
from common.game import Game
from common.player import Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.first_player = Player(State.white, self.board)
        self.second_player = Player(State.black, self.board)
        self.game = Game(self.board, self.first_player, self.second_player)

    def test_initialize(self):
        self.assertEqual(self.game.first_player.colour, State.white)
        self.assertEqual(self.game.second_player.colour, State.black)
        self.assertEqual(self.game.current_player_colour, State.black)

    def test_get_current_player(self):
        self.assertEqual(self.game.get_current_player(), self.second_player)

    def test_get_other_player(self):
        self.assertEqual(self.game.get_other_player(), self.first_player)

    def test_is_game_won_should_return_false(self):
        self.assertFalse(self.game.is_game_won())

    def test_is_game_won_should_return_true(self):
        for x in range(8):
            for y in range(8):
                self.board.make_white(x, y)
        self.assertTrue(self.game.is_game_won())

    def test_get_winner_should_return_none(self):
        self.assertEqual(self.game.get_winner(), None)

    def test_change_current_player(self):
        self.game.change_current_player()
        self.assertEqual(self.game.get_current_player(), self.first_player)
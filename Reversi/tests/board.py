import unittest
from common.board import *
from common.state import State


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialize(self):
        self.assertEqual(self.board.width, 8)
        self.assertEqual(self.board.height, 8)
        self.assertEqual(len(self.board.pieces), 8)

        self.assertEqual(self.board.pieces[0][0].state, State.empty)

        for row in self.board.pieces:
            self.assertEqual(len(row), 8)

    def test_center_colours(self):
        self.assertEqual(self.board.pieces[3][3].state, State.white)
        self.assertEqual(self.board.pieces[3][4].state, State.black)
        self.assertEqual(self.board.pieces[4][3].state, State.black)
        self.assertEqual(self.board.pieces[4][4].state, State.white)

    def test_is_on_board_when_inside(self):
        self.assertTrue(self.board.is_inside(3, 3))

    def test_is_on_board_when_outside(self):
        self.assertFalse(self.board.is_inside(8, 8))

    def test_is_valid_move_not_inside(self):
        self.assertFalse(self.board.is_valid_move(8, 8, State.black))

    def test_is_valid_move_on_not_empty_piece(self):
        self.assertFalse(self.board.is_valid_move(3, 3, State.black))

    def test_is_valid_move_on_emty_piece(self):
        self.assertFalse(self.board.is_valid_move(1, 1, State.black))

    def test_is_valid_move_on_emty_piece_7_7(self):
        self.assertFalse(self.board.is_valid_move(7, 7, State.black))

    def test_is_valid_move_on_emty_piece_color_not_changed(self):
        self.board.is_valid_move(1, 1, State.black)

        self.assertEqual(self.board.pieces[1][1].state, State.empty)

    def test_is_valid_move_on_emty_piece_2_3(self):
        pieces = self.board.is_valid_move(2, 3, State.black)
        self.assertEqual(1, len(pieces))

    def test_is_valid_move_on_emty_piece_2_3_invalid(self):
        pieces = self.board.is_valid_move(2, 3, State.white)
        self.assertFalse(pieces)

    def test_is_valid_move_on_emty_piece_2_2(self):
        pieces = self.board.is_valid_move(2, 3, State.black)
        self.assertEqual(1, len(pieces))

    def test_is_valid_move_on_emty_piece_4_5(self):
        pieces = self.board.is_valid_move(4, 5, State.black)
        self.assertEqual(1, len(pieces))

    def test_get_valid_moves_black(self):
        valid_moves = self.board.get_valid_moves(State.black)
        self.assertEqual((2, 3), valid_moves[0])
        self.assertEqual((3, 2), valid_moves[1])
        self.assertEqual((4, 5), valid_moves[2])
        self.assertEqual((5, 4), valid_moves[3])

    def test_get_valid_moves_white(self):
        valid_moves = self.board.get_valid_moves(State.white)
        self.assertEqual((2, 4), valid_moves[0])
        self.assertEqual((3, 5), valid_moves[1])
        self.assertEqual((4, 2), valid_moves[2])
        self.assertEqual((5, 3), valid_moves[3])

    def test_make_black(self):
        self.board.make_black(1, 1)
        self.assertEqual(self.board.pieces[1][1].state, State.black)

    def test_make_white(self):
        self.board.make_white(1, 1)
        self.assertEqual(self.board.pieces[1][1].state, State.white)

    def test_make_empty(self):
        self.board.make_empty(3, 3)
        self.assertEqual(self.board.pieces[3][3].state, State.empty)

    def test_change_piece_sets_black(self):
        self.board.change_piece(1, 1, State.black)
        self.assertEqual(self.board.pieces[1][1].state, State.black)

    def test_change_piece_sets_white(self):
        self.board.change_piece(1, 1, State.white)
        self.assertEqual(self.board.pieces[1][1].state, State.white)

    def test_change_piece_sets_empty(self):
        self.board.change_piece(3, 3, State.empty)
        self.assertEqual(self.board.pieces[3][3].state, State.empty)

    def test_reset(self):
        self.board.make_empty(3, 3)
        self.board.make_empty(3, 4)
        self.board.make_empty(4, 3)
        self.board.make_empty(4, 4)
        self.board = self.board.reset()
        self.assertEqual(self.board.pieces[3][3].state, State.white)
        self.assertEqual(self.board.pieces[3][4].state, State.black)
        self.assertEqual(self.board.pieces[4][3].state, State.black)
        self.assertEqual(self.board.pieces[4][4].state, State.white)

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget
from gui.dialogs.main_window import *
from common.player import *
from common.state import *
from common.game import *
from common.computer import *

MENU_TITLE = "Menu"


class MenuDialog(QWidget):

    def __init__(self, board):
        super().__init__()

        self.board = board
        self.setWindowTitle(MENU_TITLE)
        # self.game_window = MainWindow(game)
        againstComputer = QPushButton("&Play against Computer")
        againstComputer.setFocusPolicy(Qt.NoFocus)
        againstComputer.clicked.connect(self.start_against_computer)

        againstPlayer = QPushButton("&Play against another Player")
        againstPlayer.setFocusPolicy(Qt.NoFocus)
        againstPlayer.clicked.connect(self.start_against_player)

        whatComputersPlay = QPushButton("&Watch two computers play")
        whatComputersPlay.setFocusPolicy(Qt.NoFocus)
        whatComputersPlay.clicked.connect(self.start_watch_computers)

        layout = QGridLayout()
        layout.addWidget(againstPlayer, 0, 1)
        layout.addWidget(againstComputer, 1, 1)
        layout.addWidget(whatComputersPlay, 2, 1)
        self.setLayout(layout)
        self.resize(400, 400)

    def start_against_player(self):
        first_player = Player(State.white, self.board)
        second_player = Player(State.black, self.board)
        game = Game(self.board, first_player, second_player)

        self.game_window = MainWindow(game)
        self.game_window.show()
        self.hide()

    def start_against_computer(self):
        first_player = Computer(State.white, self.board)
        second_player = Player(State.black, self.board)
        game = Game(self.board, first_player, second_player)

        self.game_window = MainWindow(game)
        self.game_window.show()
        self.hide()

    def start_watch_computers(self):
        first_player = Computer(State.white, self.board)
        second_player = Computer(State.black, self.board)
        game = Game(self.board, first_player, second_player)

        self.game_window = MainWindow(game)
        self.game_window.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuDialog()
    window.show()
    sys.exit(app.exec_())

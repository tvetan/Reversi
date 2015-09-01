import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

MENU_TITLE = "Menu"


class MenuDialog(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(MENU_TITLE)
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
        layout.addWidget(againstComputer, 0, 1)
        layout.addWidget(againstPlayer, 1, 1)
        layout.addWidget(whatComputersPlay, 2, 1)
        self.setLayout(layout)
        self.resize(400, 400)

    def start_against_computer(self):
        pass

    def start_against_player(self):
        pass

    def start_watch_computers(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuDialog()
    window.show()
    sys.exit(app.exec_())

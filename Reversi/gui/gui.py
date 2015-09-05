import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from gui.dialogs.menu_dialog import *
from PyQt5.QtGui import QCursor


class Gui():

    def __init__(self, game):
        self.game = game

    def show(self):
        app = QApplication(sys.argv)
        QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))
        window = MenuDialog(self.game)
        window.show()
        sys.exit(app.exec_())

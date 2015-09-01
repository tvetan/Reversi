from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QWidget
import sys
import os


WINDOW_TITLE = "Reversi"


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.center()

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.resize(400, 400)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    val = app.exec()
    os._exit(val)

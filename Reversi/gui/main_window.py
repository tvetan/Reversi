from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import sys
import os


WINDOW_TITLE = "Reversi"


class MainWindow():

    def setup_ui(self, window):
        window.setWindowTitle(WINDOW_TITLE)
        window.resize(400, 400)

    def center(self, window):
        qr = window.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        window.move(qr.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(main_window)
    ui.center(main_window)
    main_window.show()
    val = app.exec()
    os._exit(val)

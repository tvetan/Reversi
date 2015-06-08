from PyQt5 import QtWidgets
import sys
import os


class MainWindow():

    def setup_ui(self, window):
        window.setObjectName("Reversi")
        window.resize(500, 500)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    val = app.exec()
    os._exit(val)

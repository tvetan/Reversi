from gui.main_window import *


class Gui():

    def __init__(self):
        self.mainWindow = MainWindow()

    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()

        self.mainWindow.setup_ui(main_window)
        main_window.show()
        val = app.exec()
        os._exit(val)

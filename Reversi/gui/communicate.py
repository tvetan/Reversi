from PyQt5.QtCore import QObject, pyqtSignal


class Communicate(QObject):

    def __init__(self):
        super(Communicate, self).__init__()

    clicked = pyqtSignal(str)
    reset_game = pyqtSignal()
    message_statusbar = pyqtSignal(str)

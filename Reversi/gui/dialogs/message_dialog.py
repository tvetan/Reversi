from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog


class MessageDialog(QDialog):

    def __init__(self, message):
        super().__init__()

        self.label = QLabel()
        self.label.setText(message)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 1)

        self.setLayout(layout)

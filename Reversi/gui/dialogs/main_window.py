from PyQt5.QtWidgets import (QDesktopWidget,
                             QMainWindow,
                             QAction, QFrame)
from PyQt5.QtGui import (QPalette, QPen,
                         QIcon, QPainter, QColor)
from PyQt5.QtCore import Qt, QBasicTimer, QPoint
from gui.communicate import Communicate
from common.state import State
from gui.dialogs.message_dialog import *
from common.computer import Computer
from gui.dialogs.board_ui import *
import time


WINDOW_TITLE = "Reversi"
WINDOWHEIGHT = 480
WINDOWWIDTH = 640
SPACE = 50
WIDTH = 8
HEIGHT = 8
X_OFFSET = int((WINDOWWIDTH - 400) / 2)
Y_OFFSET = int((WINDOWHEIGHT - 440) / 2)
PLAYERS_STATES = [State.black, State.white]


class MainWindow(QMainWindow):

    def __init__(self, game):
        super().__init__()
        self.setup_ui()
        self.center()

        self.game = game           
                
        self.setMouseTracking(True)
        self.board_ui = BoardUi(self, self.game)
        self.init_status_bar()
        self.set_menubar()
        self.setCentralWidget(self.board_ui)

        self.set_background_color()

        self.board_ui.start()

    def set_menubar(self):
        newGameAction = QAction(QIcon('new.png'), '&New Game', self)
        newGameAction.setShortcut('Ctrl+N')
        newGameAction.setStatusTip('New Game')
        newGameAction.triggered.connect(self.board_ui.restart_game)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&New')
        fileMenu.addAction(newGameAction)

    def setup_ui(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.setFixedSize(WINDOWWIDTH, WINDOWHEIGHT)

    def center(self):
        frame = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())

    def mouseMoveEvent(self, event):
        self.communicate.clicked.emit(str(event.pos()))

    def set_background_color(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.white)
        self.setPalette(palette)

    def init_status_bar(self):
        self.communicate = Communicate()
        self.statusbar = self.statusBar()
        self.communicate.message_statusbar[str]\
            .connect(self.statusbar.showMessage)
        self.communicate.message_statusbar.emit(
            self.board_ui.get_current_player_message())


# class BoardUi(QFrame):

#     def __init__(self, parent, game):
#         super().__init__(parent)
#         self.main_window = parent
#         self.game = game

#     def start(self):
#         self.show()
#         self.setFocusPolicy(Qt.StrongFocus)
#         self.timer = QBasicTimer()
#         self.timer.start(150, self)
#         if isinstance(self.game.first_player, Computer) \
#             and isinstance(self.game.second_player, Computer):
#             self.computers_play()

#     def computers_play(self):
#         while not self.game.is_game_won():
#             self.computer_turn()
#         #self.show_winner_message()

#     def init_signals(self):
#         self.communicate = Communicate()
#         self.communicate.restart.connect(self.restart_game)

#     def paintEvent(self, e):
#         painter = QPainter()
#         painter.begin(self)
#         self.draw_board_rectangle(painter)
#         painter.end()

#     def draw_board_rectangle(self, painter):
#         col = QColor(0, 0, 0)
#         col.setNamedColor('#d4d4d4')
#         painter.setPen(col)

#         painter.setBrush(QColor(200, 0, 0))
#         painter.drawRect(X_OFFSET, Y_OFFSET, 400, 400)

#         pen = QPen(Qt.black, 2, Qt.SolidLine)

#         painter.setPen(pen)
#         for spot in [(x, x) for x in range(WIDTH + 1)]:
#             left = ((spot[0] * SPACE) + X_OFFSET, Y_OFFSET)
#             right = ((spot[0] * SPACE) + X_OFFSET, Y_OFFSET + (HEIGHT * SPACE))
#             up = (X_OFFSET, (spot[1] * SPACE) + Y_OFFSET)
#             down = (X_OFFSET + (WIDTH * SPACE), (spot[1] * SPACE) + Y_OFFSET)
#             painter.drawLine(left[0], left[1], right[0], right[1])
#             painter.drawLine(up[0], up[1], down[0], down[1])

#         for x in range(WIDTH):
#             for y in range(HEIGHT):
#                 centerx, centery = self.get_center(x, y)
#                 if self.game.board.pieces[x][y].state in PLAYERS_STATES:
#                     if self.game.board.pieces[x][y].state == State.white:
#                         painter.setBrush(Qt.white)
#                     else:
#                         painter.setBrush(Qt.black)
#                     center = QPoint(centerx, centery)

#                     circle_diameter = int(SPACE / 2) - 5
#                     painter.drawEllipse(
#                         center, circle_diameter, circle_diameter)

#     def get_center(self, x, y):
#         return X_OFFSET + x * SPACE + int(SPACE / 2), \
#             Y_OFFSET + y * SPACE + int(SPACE / 2)

#     def timerEvent(self, event):
#         self.update()

#     def get_clicked_block_position(self, mouseX, mouseY):
#         for x in range(WIDTH):
#             for y in range(HEIGHT):
#                 if mouseX > x * SPACE + X_OFFSET and \
#                    mouseX < (x + 1) * SPACE + X_OFFSET and \
#                    mouseY > y * SPACE + Y_OFFSET and \
#                    mouseY < (y + 1) * SPACE + Y_OFFSET:
#                     return (x, y)

#         return None

#     def mousePressEvent(self, event):
#         if isinstance(self.game.get_current_player(), Computer):
#             return

#         position = event.pos()
#         piece_position = self.get_clicked_block_position(
#             position.x(), position.y())

#         if piece_position is None:
#             return

#         current_player = self.game.get_current_player()
#         other_player = self.game.get_other_player()

#         is_valid = current_player.make_move(
#             piece_position[0], piece_position[1], other_player)

#         if not is_valid:
#             return

#         self.game.change_current_player()

#         if self.game.is_game_won():
#             self.show_winner_message()
#             return

#         if isinstance(self.game.get_current_player(), Computer):
#             self.computer_turn()

#         message = str(
#             self.get_current_player_message()
#                 + " | Scores: " + self.get_score_text())
#         self.main_window.communicate.message_statusbar.emit(message)

#     def get_current_player_message(self):
#         if self.game.first_player.colour == self.game.current_player_colour:
#             return "First player's turn with " \
#                 + self.game.current_player_colour.name

#         return "Second player's turn with " \
#             + self.game.current_player_colour.name

#     def show_winner_message(self):
#         winner = self.game.get_winner()
#         message = None
#         if winner is None:
#             message = "No one won its a tie"
#         elif winner is self.game.first_player:
#             message = "First Player has won"
#         else:
#             message = "Second Player has won"

#         self.main_window.communicate.message_statusbar.emit(message)

#     def get_score_text(self):
#         text = 'Player 1: %s    Player 2: %s'
#         first_player_score = self.game.first_player.score
#         second_player_score = self.game.second_player.score

#         return text % (first_player_score, second_player_score)

#     def restart_game(self):
#         self.game.reset_game()
#         self.update()
#         message = str(
#             self.get_current_player_message()
#             + " | Scores: " + self.get_score_text())
#         self.main_window.communicate.message_statusbar.emit(message)

#     def computer_turn(self):
#         current_player = self.game.get_current_player()
#         other_player = self.game.get_other_player()
#         current_player.make_move(other_player)
#         self.game.change_current_player()

#         # if self.game.is_game_won():
#         #     self.show_winner_message()

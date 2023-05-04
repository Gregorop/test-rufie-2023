#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *

from instr import *


class FinalWin(QWidget):
    def __init__(self, age, p1,p2,p3):
        super().__init__()
        self.set_appear()
        self.set_ui()
        print(age, p1,p2,p3)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def set_ui(self):
        index = QLabel('Ваш индекс Руфье:')
        health = QLabel('тут будет оценка здоровья')
        
        line = QVBoxLayout()
        line.addWidget(index)
        line.addWidget(health)

        self.setLayout(line)
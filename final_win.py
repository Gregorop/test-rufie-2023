#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *

from instr import *


class FinalWin(QWidget):
    def __init__(self, age, p1,p2,p3):
        super().__init__()
        self.index = self.calc_index(p1, p2, p3)
        self.health = self.calc_health(age, self.index)
        self.set_appear()
        self.set_ui()

    def calc_health(self, age, index):
        if age > 15:
            if index > 15: return 'низкое'
            elif index > 6: return 'средний'
            else: return 'высокий'
        else:
            if index > 18: return 'низкое'
            elif index > 9: return 'средний'
            else: return 'высокий'

    def calc_index(self, p1,p2,p3):
        return ((p1+p2+p3)*4 - 200)/10

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def set_ui(self):
        index = QLabel('Ваш индекс Руфье: ' + str(self.index))
        health = QLabel('Ваше здоровье: ' + self.health)
        
        line = QVBoxLayout()
        line.addWidget(index)
        line.addWidget(health)

        self.setLayout(line)
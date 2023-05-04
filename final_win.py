#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from settings import *


class FinalWin(QWidget):
    def __init__(self, age, p1, p2, p3):
        super().__init__()
        self.index = self.calc_index(p1, p2, p3)
        self.health = self.calc_health(age, self.index)
        self.set_appear()
        self.set_ui()
        

    def calc_index(self, p1, p2, p3):
        return ((p1+p2+p3)*4 - 200)/10

    def calc_health(self, age, index):
        if age > 15:
            if index > 15 : return 'Низкий'
            if index > 6 : return 'Средний'
            else: return 'Высокий'
        else:
            if index > 18 : return 'Низкий'
            if index > 9 : return 'Средний'
            else: return 'Высокий'

    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)

    def set_ui(self):
        final_res = QLabel(final + str(self.index))
        health = QLabel(txt_health + self.health)

        line = QVBoxLayout()
        line.addWidget(final_res)
        line.addWidget(health)
        
        self.setLayout(line)
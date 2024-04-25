#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *

from instr import *


class FinalWin(QWidget):
    def __init__(self, age, p1,p2,p3):
        super().__init__()
        self.index = self.calc_index(p1, p2, p3)
        self.index2 = self.calc_index2(p1, p2, p3)
        self.health = self.calc_health(age, self.index)
        self.health2 = self.calc_health(age, self.index2)
        self.set_appear()

        self.set_ui()

    def calc_health(self, age, index):
        if age > 15:
            if index > 15: return 'низкое'
            elif index > 6: return 'среднее'
            else: return 'высокое'
        else:
            if index > 18: return 'низкое'
            elif index > 9: return 'среднее'
            else: return 'высокое'
    def calc_health2(self, age, index):
        
            if 0.1 < index <5: return 'хорошее'
            if 5.1 < index > 10: return 'среднее'
            if 10.1 < index < 15: return 'удовлетворительное'
            if index > 15: return 'плохое'
        

    def calc_index(self, p1,p2,p3):
        return ((p1+p2+p3)*4 - 200)/10
    
    def calc_index2(self, p1,p2,p3): #считает по разному
        return ((p2-70)+(p3-p1))/10

    def set_appear(self):
        self.setStyleSheet('font-size:38px;')
        if self.health == 'низкое':
            self.setStyleSheet('font-size:38px; background:pink')
        if self.health == 'высокое':
            self.setStyleSheet('font-size:38px; background:lightgreen')    
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def set_ui(self):
        index = QLabel('Ваш индекс Руфье: ' + str(self.index))
        index2 = QLabel('Ваш индекс Руфье-Диксона: ' + str(self.index2))
        health = QLabel('Ваше здоровье: ' + self.health)
        health2 = QLabel('Ваше здоровье: ' + self.health2)
        
        line = QVBoxLayout()
        line.addWidget(index)
        line.addWidget(health)

        line.addWidget(index2)
        line.addWidget(health2)


        self.setLayout(line)
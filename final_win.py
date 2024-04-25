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
            if index > 15: return 'низкий'
            elif 11 < index <= 15: return 'удовлетворительный'
            elif 6 < index <= 11: return 'средний'
            elif 0.5 < index <= 6: return 'выше среднего'
            else: return 'высокий'

        if 13 <= age <= 14:
            if index > 16.5: return 'низкий'
            elif 12.5 < index <= 16.5: return 'удовлетворительный'
            elif 7.5 < index <= 12.5: return 'средний'
            elif 2 < index <= 7.5: return 'выше среднего'
            else: return 'высокий'

        if 11 <= age <= 12:
            if index > 18: return 'низкий'
            elif 14 < index <= 18: return 'удовлетворительный'
            elif 9 < index <= 14: return 'средний'
            elif 3.5 < index <= 9: return 'выше среднего'
            else: return 'высокий'

        if 9 <= age <= 10:
            if index > 19.5: return 'низкий'
            elif 15.5 < index <= 19.5: return 'удовлетворительный'
            elif 10.5 < index <= 15.5: return 'средний'
            elif 5 < index <= 10.5: return 'выше среднего'
            else: return 'высокий'
        
        if 7 <= age <= 8:
            if index > 21: return 'низкий'
            elif 17 < index <= 21: return 'удовлетворительный'
            elif 12 < index <= 17: return 'средний'
            elif 6.5 < index <= 12: return 'выше среднего'
            else: return 'высокий'
        

    def calc_index(self, p1,p2,p3):
        return ((p1+p2+p3)*4 - 200)/10

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
        health = QLabel('Ваше здоровье: ' + self.health)
        
        line = QVBoxLayout()
        line.addWidget(index)
        line.addWidget(health)

        self.setLayout(line)
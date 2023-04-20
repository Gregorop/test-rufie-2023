#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from settings import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()


    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)

    def set_ui(self):
        final_res = QLabel(final)
        health = QLabel(txt_health)

        line = QVBoxLayout()
        line.addWidget(final_res)
        line.addWidget(health)
        
        self.setLayout(line)
#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *

from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def set_ui(self):
        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        age_input = QLineEdit()
        instr1 = QLabel(txt_test1)
        start1_btn = QPushButton(txt_starttest1)

        line = QVBoxLayout()
        line.addWidget(fio_label)
        line.addWidget(fio_input)
        line.addWidget(age_label)
        line.addWidget(age_input)
        line.addWidget(instr1)
        line.addWidget(start1_btn)
        self.setLayout(line)
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
        timer_label = QLabel('00:00:15')

        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        age_input = QLineEdit()
        instr1 = QLabel(txt_test1)
        start1_btn = QPushButton(txt_starttest1)

        puls1_input = QLineEdit()
        instr2 = QLabel(txt_test2)
        start2_btn = QPushButton(txt_starttest2)

        instr3 = QLabel(txt_test3)
        start3_btn = QPushButton(txt_starttest3)

        puls2_input = QLineEdit()
        puls3_input = QLineEdit()

        final_btn = QPushButton(txt_sendresults)

        line = QVBoxLayout()
        line.addWidget(timer_label)
        line.addWidget(fio_label)
        line.addWidget(fio_input)
        line.addWidget(age_label)
        line.addWidget(age_input)
        line.addWidget(instr1)
        line.addWidget(start1_btn)
        line.addWidget(puls1_input)
        line.addWidget(instr2)
        line.addWidget(start2_btn)
        line.addWidget(instr3)
        line.addWidget(start3_btn)
        line.addWidget(puls2_input)
        line.addWidget(puls3_input)
        line.addWidget(final_btn)
        self.setLayout(line)
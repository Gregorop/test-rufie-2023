from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from settings import *
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()


    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)

    def set_ui(self):
        timer_label = QLabel('00:00:15')
        timer_label.setStyleSheet("font-size: 35px")
        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        age_input = QLineEdit()
        instr1 = QLabel(txt_instr1)
        start_btn1 = QPushButton(txt_start_btn1)

        pulse1_input = QLineEdit()
        instr2 = QLabel(txt_instr2)
        test = QPushButton(txt_test)
        instr3 = QLabel(txt_instr3)
        test2 = QPushButton(txt_test2)
        final_input1 = QLineEdit()
        final_input2 = QLineEdit()
        results = QPushButton(txt_next_results)



        line2 = QHBoxLayout()
        line = QVBoxLayout()
        
        line.addWidget(fio_label)
        line.addWidget(fio_input, alignment= Qt.AlignLeft)
        line.addWidget(age_label)
        line.addWidget(age_input, alignment= Qt.AlignLeft)
        line.addWidget(instr1)
        line.addWidget(start_btn1, alignment= Qt.AlignLeft)
        line.addWidget(pulse1_input, alignment= Qt.AlignLeft)
        line.addWidget(instr2)
        line.addWidget(test, alignment= Qt.AlignLeft)
        line.addWidget(instr3)
        line.addWidget(test2, alignment= Qt.AlignLeft)
        line.addWidget(final_input1, alignment= Qt.AlignLeft)
        line.addWidget(final_input2, alignment= Qt.AlignLeft)
        line.addWidget(results, alignment= Qt.AlignCenter)
        line2.addLayout(line)
        line2.addWidget(timer_label, alignment= Qt.AlignRight) 



        
        self.setLayout(line2)
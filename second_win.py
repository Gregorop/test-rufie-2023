from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTimer

from settings import *
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()

    def test1 (self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('hh:mm:ss'))
        if self.time.second() == 0:
            self.timer.stop()



    def start_timer1(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 15)
        self.timer.start(1000)
        self.timer.timeout.connect(self.test1)

    def test2 (self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('ss'))
        self.timer_label.setStyleSheet('color:lightgreen; font-size: 35px')
        if self.time.second() == 0:
            self.timer.stop()



    def start_timer2(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 45)
        self.timer.start(1000)
        self.timer.timeout.connect(self.test2)

    def test3 (self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('hh:mm:ss'))
        self.timer_label.setStyleSheet('color:lightgreen; font-size: 35px')
        if self.time.second() <= 45:
            self.timer_label.setStyleSheet('color:black; font-size: 35px')
        if self.time.second() <= 15:
            self.timer_label.setStyleSheet('color:lightgreen; font-size: 35px')
        if self.time.second() == 0:
            self.timer.stop()



    def start_timer3(self):
        self.timer = QTimer()
        self.time = QTime(0, 1, 0)
        self.timer.start(1000)
        self.timer.timeout.connect(self.test3)






    def set_appear(self):
        self.setWindowTitle(title)
        self.resize(win_width, win_height)

    def set_ui(self):
        self.timer_label = QLabel('00:00:15')
        self.timer_label.setStyleSheet("font-size: 35px")
        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        age_input = QLineEdit()
        instr1 = QLabel(txt_instr1)
        start_btn1 = QPushButton(txt_start_btn1)
        start_btn1.clicked.connect(self.start_timer1)

        pulse1_input = QLineEdit()
        instr2 = QLabel(txt_instr2)
        test = QPushButton(txt_test)
        test.clicked.connect(self.start_timer2)
        instr3 = QLabel(txt_instr3)
        test2 = QPushButton(txt_test2)
        test2.clicked.connect(self.start_timer3)
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
        line2.addWidget(self.timer_label, alignment= Qt.AlignRight) 



        
        self.setLayout(line2)

#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QTimer

from instr import *

class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def test_1(self):
        self.time = self.time.addSecs(-1)
        self.timer_label.setText(self.time.toString('mm:ss'))
        if self.time.second() == 0:
            self.timer.stop()
            self.timer_label.setText('этап 1 закончен')

    def start_timer_1(self): #запускаем таймер 1
        self.timer = QTimer()
        self.time = QTime(0,0,15)
        self.timer.start(1000) #1000 милисекунд = раз в 1 нормальную секунду
        self.timer.timeout.connect(self.test_1)       #запускается метод test

    def set_ui(self):
        self.timer_label = QLabel('00:00:15')

        fio_label = QLabel(txt_name)
        fio_input = QLineEdit()
        age_label = QLabel(txt_hintage)
        age_input = QLineEdit()
        instr1 = QLabel(txt_test1)
        start1_btn = QPushButton(txt_starttest1)

        #тут функция чтобы запустить отчет таймера
        start1_btn.clicked.connect(self.start_timer_1) 

        puls1_input = QLineEdit()
        instr2 = QLabel(txt_test2)
        start2_btn = QPushButton(txt_starttest2)

        instr3 = QLabel(txt_test3)
        start3_btn = QPushButton(txt_starttest3)

        puls2_input = QLineEdit()
        puls3_input = QLineEdit()

        final_btn = QPushButton(txt_sendresults)

        line = QVBoxLayout()
        line.addWidget(self.timer_label)
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
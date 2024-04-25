#тут будут 3 класса, для каждого окна
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from second_win import *

from instr import *

class FirstWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.set_ui()

    def set_appear(self):
        self.setStyleSheet('font-size:34px; background:lightgreen')
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def show_second_win(self):
        self.win = SecondWin()
        self.win.show()
        self.hide()

    def set_ui(self):
        hello = QLabel(txt_hello)
        instruction = QLabel(txt_instruction)
        start_btn = QPushButton(txt_next)
        
        start_btn.setStyleSheet('''width:200px;height:200px;background:pink''')
        #start_btn.setFixedWidth(35) 
        start_btn.clicked.connect(self.show_second_win)
        
        line = QVBoxLayout()
        line.addWidget(hello, alignment=Qt.AlignCenter)
        line.addWidget(instruction)
        line.addWidget(start_btn, alignment=Qt.AlignCenter)
        self.setLayout(line)
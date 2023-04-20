#этот файл будет все запускать
from first_win import *
from second_win import *

app = QApplication([])

first = FirstWin()
first.show()

second = SecondWin()
second.show()

app.exec()
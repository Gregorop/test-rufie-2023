#этот файл будет все запускать
from first_win import *

app = QApplication([])

first = FirstWin()
first.show()

app.exec_()
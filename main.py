#этот файл будет все запускать
from first_win import * 
from second_win import *
from final_win import *

app = QApplication([])

first = FirstWin()
first.hide()

second = SecondWin()
second.show()

final = FinalWin()
final.hide()

app.exec()
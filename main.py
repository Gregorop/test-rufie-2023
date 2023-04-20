#этот файл будет все запускать
from first_win import * 
from second_win import *
from final_win import *

app = QApplication([])

first = FirstWin()
first.show()

second = SecondWin()
second.show()

final = FinalWin()
final.show()

app.exec()
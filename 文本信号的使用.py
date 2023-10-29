#***************常用信号****************************
#textEdited(text)  文本编辑时发射的信号
#textChanged(text) 文本框文本发生改变时发出的信号
#returnPressed()按下回车键时发出的信号
#editingFinished() 结束编辑时发出的信号

#cursorPositionChanged(int OldPos,int NewPos)光标位置发生改变时发出的信号
#selectionChanged()选中的文本发生改变时发出的信号
#***************常用信号****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('信号的使用')
window.resize(500,500)

le=QLineEdit(window)
le.move(150,150)

le.textChanged.connect(lambda :print(666666666))

def set():
    le2.setFocus()
le.returnPressed.connect(set)

le2=QLineEdit(window)
le2.move(150,200)
def put():
    le.setFocus()
le2.returnPressed.connect(put)



window.show()
sys.exit(app.exec_())


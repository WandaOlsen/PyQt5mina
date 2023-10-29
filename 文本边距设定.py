from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('文本边距设定')
window.resize(500,500)

le=QLineEdit(window)
le.move(50,50)
le.resize(300,300)
le.setStyleSheet('background-color:cyan;')
# le.setContentsMargins(100,0,0,0)
le.setTextMargins(100,200,0,0)          #四个数字代表距离左上右下的距离


window.show()
sys.exit(app.exec_())
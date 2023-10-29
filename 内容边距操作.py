from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('333')
window.resize(500,500)

label=QLabel(window)
label.setText('anaconda3')
label.resize(300,300)
label.setStyleSheet('background-color:cyan;')
label.setContentsMargins(100,200,0,0)         #设置内容区域   文本内容展示在内容区域水平靠左垂直居中
print(label.contentsRect())







window.show()
sys.exit(app.exec_())
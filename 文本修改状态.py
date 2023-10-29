from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('修改状态')
window.resize(500,500)

le=QLineEdit(window)
le.move(150,150)

def chao():
    print(le.isModified())   #查看文本框是否处于被编辑状态
    le.setModified(False)     #设置文本编辑状态

btn=QPushButton(window)
btn.setText('按钮')
btn.move(180,250)
btn.clicked.connect(chao)


window.show()
sys.exit(app.exec_())
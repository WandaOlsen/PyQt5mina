from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()

window.move(200,200)   #move里面指的是边框左上角相对桌面左上角的坐标
window.resize(150,150)  #resize设置的是用户区域的大小
window.setFixedSize(500,500)  #设置固定大小

label=QLabel(window)
label.setText('雨纷纷')
label.move(200,200)
label.setStyleSheet('background-color:red')

def chao():
    new_text=label.text()+'旧故里草木深'
    label.setText(new_text)
    label.adjustSize()
btn=QPushButton(window)
btn.setText('请点击按钮')
btn.move(300,200)
btn.clicked.connect(chao)




window.show()
#window.setGeometry(0,0,150,150)    #用户区域距离左上角的坐标以及尺寸
sys.exit(app.exec_())
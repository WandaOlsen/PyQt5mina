#***************创建一个窗口包含一个标签****************************
#要求：鼠标进入标签时展示“欢迎光临”，鼠标离开标签时，展示“谢谢惠顾”。
#***************创建一个窗口包含一个标签****************************
from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def enterEvent(self,*args,**kwargs):
        print('鼠标进入')
        self.setText('欢迎光临')

    def leaveEvent(self,*args,**kwargs):
        print('鼠标离开')
        self.setText('谢谢惠顾')
        

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

label=MyLabel(window)
label.resize(200,200)
label.setStyleSheet('background-color:cyan;')
label.move(100,100)





window.show()
sys.exit(app.exec_())
#***************设计一个窗口，并使其按一定时间间隔不断放大****************************

#***************设计一个窗口，并使其按一定时间间隔不断放大****************************
from PyQt5.Qt import *
import sys
import os

def set():
    os.system(r'python D:\\Python\\爬虫初调\\李峋版爱心代码.py')
class MyWidget(QWidget):
    def timerEvent(self,*args,**kwargs):
        current_w=self.width()
        current_h=self.height()
        self.resize(current_w + 10,current_h + 10)

        if current_w == 2400:
            print('hold补助啦')
            self.killTimer(timer_id)

app=QApplication(sys.argv)

window=MyWidget()
window.setWindowTitle('333')
window.resize(200,200)
window.move(0,0)
timer_id=window.startTimer(100)

label=QLabel(window)
label.setText('新年快乐\n吃好喝好')
label.setStyleSheet('font-size:450px;color:red')
window.destroyed.connect(set)
window.show()
sys.exit(app.exec_())
#***************创建一个窗口，并设置一个子控件QLabel****************************
#要求：展示10s倒计时；倒计时结束，就停止计时
#
#***************创建一个窗口，并设置一个子控件QLabel****************************
from PyQt5.Qt import *
import sys
import os

def set():
    os.system(r'python "D:\\Python\\GUI PyQt5\\定时器案例2.py"')

class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText('10')
        self.move(145, 120)
        self.setStyleSheet('font-size:300px;')
        self.timer_id=self.startTimer(1000)
        self.destroyed.connect(set)
    def setSec(self,sec):
        self.setText(str(sec))

    def startMyTimer(self,ms):
        self.startTimer(ms)

    def timerEvent(self,*args,**kwargs):
        #print('xx')
        current_sec=int(self.text())         #获取当前的标签内容并把其转换为int类型
        current_sec-=1                      #将current_sec减一
        self.setText(str(current_sec))         #设置标题为减一过后并且转换为字符串格式的current_sec

        if current_sec == 0:
            print('计时结束')
            self.killTimer(self.timer_id)

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('计时器')
window.resize(500,500)

label=MyLabel(window)
# label.setText('10')
# label.move(55,50)
# label.setStyleSheet('font-size:78px;')
# label.setSec(10)
# label.startMyTimer(500)

#label.startTimer(1000)      #每隔1秒都会去执行label对象内部的timerEvent


window.show()
sys.exit(app.exec_())


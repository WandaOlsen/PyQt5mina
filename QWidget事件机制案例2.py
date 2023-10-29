#***************创建一个窗口监听用户按键****************************
#要求：监听用户输入Tab键；监听用户输入Ctrl+S组合键；监听用户输入Ctrl+Shift+A
#***************创建一个窗口监听用户按键****************************
from PyQt5.Qt import *
import sys

class Mylabel(QLabel):
    def keyPressEvent(self,evt):
        QKeyEvent
        # if evt.key()==Qt.Key_Tab:
        #     print('用户点击了Tab键')
        # if evt.modifiers()==Qt.ControlModifier and evt.key() == Qt.Key_S:
        #     print('Ctrl+S被点击了')
        if evt.modifiers()==Qt.ControlModifier|Qt.ShiftModifier and evt.key()==Qt.Key_A:
            print('Ctrl+Shift+A被点击了')
        




app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

label=Mylabel(window)
label.resize(200,200)
label.setStyleSheet('background-color:cyan;')
label.grabKeyboard()            #用文本捕获键盘






window.show()
sys.exit(app.exec_())







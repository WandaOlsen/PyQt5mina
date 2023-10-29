#***************创建窗口，包含若干个Label控件****************************
#要求：点击哪个标签，就让哪个标签背景变红；使用父控件处理，不要自定义QLabel子类
#***************创建窗口，包含若干个Label控件****************************
from PyQt5.Qt import *
import sys

# class Label(QLabel):
#     def mousePressEvent(self,evt):
#         self.setStyleSheet('background-color:red;')

class Window(QWidget):
    def mousePressEvent(self,evt):
        local_x=evt.x()
        local_y=evt.y()
        sub_widget=self.childAt(local_x,local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet('background-color:red;')
        print('Anaconda3 Python3.9',local_x,local_y)

app=QApplication(sys.argv)

window=Window()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

for i in range(1,11):
    label=QLabel(window)
    label.setText('标签'+str(i))
    label.move(40*i,40*i)





window.show()
sys.exit(app.exec_())

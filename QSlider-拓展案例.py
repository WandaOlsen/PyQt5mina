#***************QSlider****************************
#要求：在滑块移动时，通过标签，展示滑块当前的数值，并要求标签位置，一直在滑块所在位置中间。
#***************QSlider****************************
from PyQt5.Qt import *

class Slider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.move(200, 200)
        self.resize(30, 200)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setTracking(True)
        self.set_up()

    def set_up(self):
        self.label = QLabel(self)
        self.label.setText('0')
        self.label.setStyleSheet('color:red;')
        self.label.hide()
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)  #调用父类
        x=(self.width()-self.label.width())/2
        # y=((self.maximum()-self.minimum()-self.value())/(self.maximum()-self.minimum()))*self.height()-self.label.height()
        y=(1-self.value()/(self.maximum()-self.minimum()))*(self.height()-self.label.height())
        # print(x,y)
        self.label.show()
        self.label.move(int(x),int(y))

    def mouseMoveEvent(self,evt):
        super().mouseMoveEvent(evt)
        x = (self.width() - self.label.width()) / 2
        # y=((self.maximum()-self.minimum()-self.value())/(self.maximum()-self.minimum()))*self.height()-self.label.height()
        y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.label.height())
        # print(x,y)
        # self.label.show()
        self.label.move(int(x),int(y))
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseReleaseEvent(self,evt):
        super().mouseReleaseEvent(evt)
        self.label.hide()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider 案例')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        #创建一个滑块控件，和一个标签控件
        slider=Slider(self)



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())

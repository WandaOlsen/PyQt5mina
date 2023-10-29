#***************创建一个窗口****************************
#要求：无边框无标题栏，窗口半透明，自定义最小化，最大化，关闭按钮；支持拖拽用户区移动
#***************创建一个窗口****************************
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('Anaconda3')
        self.resize(500, 500)
        self.setWindowOpacity(0.5)
        self.top_margin = 5
        self.btn_w = 80
        self.btn_h = 40
        self.setup()
    def setup(self):

        close_btn = QPushButton(self)
        self.close_btn=close_btn
        close_btn.setText('关闭')
        close_btn.resize(self.btn_w, self.btn_h)
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        # close_btn.move(close_btn_x, close_btn_y)

        max_btn = QPushButton(self)
        self.max_btn=max_btn
        max_btn.setText('最大化')
        max_btn.resize(self.btn_w, self.btn_h)
        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        # max_btn.move(max_btn_x, max_btn_y)

        mini_btn = QPushButton(self)
        self.mini_btn=mini_btn
        mini_btn.setText('最小化')
        mini_btn.resize(self.btn_w, self.btn_h)
        mini_btn_x = max_btn_x - self.btn_w
        mini_btn_y = self.top_margin
        # mini_btn.move(mini_btn_x, mini_btn_y)
        def max_nomal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText('最大化')
            else:
                self.showMaximized()
                max_btn.setText('恢复')
        close_btn.pressed.connect(self.close)
        max_btn.pressed.connect(max_nomal)
        mini_btn.pressed.connect(self.showMinimized)
    def resizeEvent(self,evt):
        print('窗口大小发生了变化')
        window_w=self.width()
        close_btn_x=window_w-self.btn_w
        close_btn_y=self.top_margin
        self.close_btn.move(close_btn_x,close_btn_y)

        max_btn_x=close_btn_x-self.btn_w
        max_btn_y=self.top_margin
        self.max_btn.move(max_btn_x,max_btn_y)

        mini_btn_x=max_btn_x-self.btn_w
        mini_btn_y=self.top_margin
        self.mini_btn.move(mini_btn_x,mini_btn_y)

    def mouseMoveEvent(self,evt):
        pass
    def mousePressEvent(self,evt):
        pass
    def mouseReleaseEvent(self,evt):
        pass


app=QApplication(sys.argv)

window=Window()



#添加三个子控件 ————窗口的右上角



window.show()
sys.exit(app.exec_())
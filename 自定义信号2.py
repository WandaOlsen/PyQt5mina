from PyQt5.Qt import *

class Btn(QPushButton):
    rightClicked=pyqtSignal()
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        if evt.button() == Qt.RightButton:
            # print('发射右击信号')
            self.rightClicked.emit()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('信号的自定义')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn=Btn('xx',self)
        btn.rightClicked.connect(lambda :print('按钮被点击了'))


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
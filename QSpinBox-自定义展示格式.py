from PyQt5.Qt import *
class SB(QSpinBox):
    def textFromValue(self,p_int):
        print(p_int)
        #1*1
        return str(p_int)+'*'+str(p_int)  #将内容展示为1*1的格式，并没有改变原本数值大小

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSpinBox自定义展示格式')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        sb=SB(self)
        self.sb=sb
        sb.resize(100,25)
        sb.move(100,100)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
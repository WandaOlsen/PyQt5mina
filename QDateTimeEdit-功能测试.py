from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDateTimeEdit')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # dte=QDateTimeEdit(self)
        # dte.move(100,100)
        # dt=QDateTime(2020,12,12,12,30) #设置时间日期
        dt=QDateTime.currentDateTime()
        dt=dt.addYears(2) #输入负数则可以减
        dte=QDateTimeEdit(dt,self)
        dte.move(100,100)
        dte.setDisplayFormat('yy-MM-dd $ mm:ss:zzz')
def main():
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())


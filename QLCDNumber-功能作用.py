from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLCDNumber')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        lcd=QLCDNumber(7,self)   #位数限制7
        lcd.move(100,100)
        lcd.resize(300,50)
        # lcd.display('AC')
        lcd.display(10)
        # lcd.setMode(QLCDNumber.Hex)
        lcd.setHexMode()


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDial')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        dia=QDial(self)
        dia.setRange(0,100)
        dia.setNotchesVisible(True)
        dia.setWrapping(True)

        label=QLabel(self)
        label.setText('Pycharm')
        label.move(200,300)
        def test(val):
            label.setStyleSheet('font-size:{}px;'.format(val))
            label.adjustSize()
        dia.valueChanged.connect(test)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
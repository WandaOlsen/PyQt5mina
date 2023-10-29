from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QAbstractSlider')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label=QLabel(self)
        label.move(100,200)
        label.setText('0')
        label.resize(80,80)

        sd=QSlider(self)
        sd.move(200,200)

        sd.valueChanged.connect(lambda val:label.setText(str(val)))
        sd.setMaximum(1000)
        sd.setMinimum(0)



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
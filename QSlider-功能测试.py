from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        sd=QSlider(self)
        sd.move(200,200)
        sd.setTickPosition(QSlider.TicksBothSides)



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
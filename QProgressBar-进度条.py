from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QProgressBar')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pb=QProgressBar(self)
        pb.move(50,200)
        pb.resize(400,50)
        print(pb.minimum())
        print(pb.maximum())
        # pb.setValue(50)
        # pb.setRange(0,0)
        pb.setRange(0,100)
        pb.setValue(0)
        # pb.setFormat('{}/%m'.format(pb.value()-pb.minimum()))
        # pb.setAlignment(Qt.AlignCenter)


        timer=QTimer(pb)
        def change():
            if pb.value()==pb.maximum():
                timer.stop()

            pb.setValue(pb.value()+10)

        timer.timeout.connect(change)
        timer.start(2000)

        pb.valueChanged.connect(lambda val:print('当前进度',val))



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
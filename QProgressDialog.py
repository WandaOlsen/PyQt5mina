from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QProgressDialog')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pd=QProgressDialog(self)
        # pd.setAutoClose(False)
        # pd.setAutoReset(False)
        pd.open()
        # for i in range(1,101):
        #     pd.setValue(i)
        pd.setValue(95)
        timer=QTimer(pd)
        def test():
            if pd.value() >= pd.maximum() or pd.wasCanceled():
                timer.stop()

            pd.setValue(pd.value() + 1)
        timer.timeout.connect(test)
        timer.start(1000)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
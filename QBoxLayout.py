from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QBoxLayout')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel('标签1')
        label1.setStyleSheet('background-color:cyan;')
        label2 = QLabel('标签2')
        label2.setStyleSheet('background-color:green;')
        label3 = QLabel('标签3')
        label3.setStyleSheet('background-color:red;')
        label4 = QLabel('标签4')
        label4.setStyleSheet('background-color:black;')

        layout=QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        self.setLayout(layout)

        timer=QTimer(self)
        def test():
            # layout.setDirection(layout.direction()+1)
            # if layout.direction()==4:
            #     layout.setDirection(0)
            #
            layout.setDirection((layout.direction() + 1)%4)
            pass

        timer.timeout.connect(test)
        timer.start(1000)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
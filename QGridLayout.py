from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QGridLayout')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        gl=QGridLayout()
        self.setLayout(gl)
        label1 = QLabel('标签1')
        label1.setStyleSheet('background-color:cyan;')
        label2 = QLabel('标签2')
        label2.setStyleSheet('background-color:green;')
        label3 = QLabel('标签3')
        label3.setStyleSheet('background-color:red;')
        label4 = QLabel('标签4')
        label4.setStyleSheet('background-color:black;')
        gl.addWidget(label1,0,0)
        gl.addWidget(label2,0,1)
        gl.addWidget(label3,1,0,2,4)
        gl.setOriginCorner(Qt.TopRightCorner)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
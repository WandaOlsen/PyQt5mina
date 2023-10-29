from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('样式表')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        layout=QVBoxLayout(self)
        label=QLabel('345')
        layout.addWidget(label)

        btn=QPushButton('234')
        layout.addWidget(btn)
        cb=QComboBox()
        cb.addItems(['1','2','3'])
        layout.addWidget(cb)
        sb=QSpinBox()
        layout.addWidget(sb)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()
    import qdarkgraystyle
    stylesheet=qdarkgraystyle.load_stylesheet_pyqt5()


    app.setStyleSheet(stylesheet)

    sys.exit(app.exec_())
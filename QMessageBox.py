from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMessageBox')
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        # mb=QMessageBox(self)
        # mb.setWindowTitle('警告！')
        # mb.setIcon(QMessageBox.Warning)
        # mb.setText('您的电脑已经中毒！')
        #
        # btn2=QPushButton('USB',mb)
        # mb.addButton(btn2,QMessageBox.NoRole)
        #
        # btn=mb.addButton('OK',QMessageBox.YesRole)
        # mb.setEscapeButton(btn)
        # mb.open()

        # QMessageBox.about(self,'123','456')
        QMessageBox.warning(self,'警告！','您的电脑已经中毒，请立即关机！')
        # QMessageBox.aboutQt(self,'345')

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())

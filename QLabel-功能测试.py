from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # le1=QLineEdit(self)
        # le1.move(100,100)
        # le2=QLineEdit(self)
        # le2.move(100,200)
        # label=QLabel('账号(&a):',self)
        label=QLabel("<a href='http://www.itlike.com'>按钮</a>",self)
        label.move(30,100)
        label.setStyleSheet('background-color:cyan;')
        # label.setBuddy(le1)
        label.resize(200,200)
        # label.setPixmap(QPixmap('躺平.jpg'))
        label.setScaledContents(True)
        label.setOpenExternalLinks(True)
        # label.setText("<img src='躺平.jpg' width=60 height=60>")
        movie=QMovie('VHF.gif')
        label.setMovie(movie)
        movie.start()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
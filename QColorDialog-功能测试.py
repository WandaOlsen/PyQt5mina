from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QColorDialog')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # self.setStyleSheet('background-color:rgb(100,200,150);')

        # self.setWindowOpacity(0.5)
        cd=QColorDialog(self)
        # cd.setWindowOpacity(0.2)
        #*******************************************
        def color():
            palette=QPalette()
            palette.setColor(QPalette.Background,cd.currentColor())
            self.setPalette(palette)
        cd.currentColorChanged.connect(color)
        # cd.setOptions(QColorDialog.ShowAlphaChannel | QColorDialog.NoButtons)
        cd.setOptions(QColorDialog.NoButtons)
        cd.show()

        btn=QPushButton(self)
        btn.move(100,100)
        btn.setText('监听按钮')
        btn.clicked.connect(lambda :print(cd.customCount()))
        #*******************************************
        return None
        #*******************************************
        def color():
            palette=QPalette()
            palette.setColor(QPalette.Background,cd.selectedColor())
            self.setPalette(palette)
        if cd.exec():
            color()
        #*******************************************
        return None
        #*******************************************
        def color():
            palette=QPalette()
            palette.setColor(QPalette.Background,cd.selectedColor())
            self.setPalette(palette)
        cd.open(color)
        #*******************************************
        return None
        #*******************************************
        def color(col):
            palette=QPalette()
            palette.setColor(QPalette.Background,col)
            self.setPalette(palette)
        cd.colorSelected.connect(color)
        #*******************************************

        cd.show()





if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
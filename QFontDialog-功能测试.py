from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFontDialog')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        font=QFont()
        font.setFamily('宋体')
        font.setPointSize(36)
        fd=QFontDialog(font,self)
        # fd.setOption(QFontDialog.NoButtons)
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        # fd = QFontDialog(self)

        btn=QPushButton(self)
        btn.setText('点击')
        btn.move(100,100)


        # fd.show()

        label=QLabel(self)
        label.move(250,100)
        label.setText('山')
        def font_sel():
            result=QFontDialog.getFont(font,self,'Anaconda3')
            if result[1]==True:
                label.setFont(result[0])
                label.adjustSize()
        btn.clicked.connect(font_sel)
        # def cfc(font):
        #     label.setFont(font)
        #     label.adjustSize()
        # fd.currentFontChanged.connect(cfc)
        # def font_sel():
        #     print('字体已经就绪',fd.selectedFont().family())
        #
        # btn.clicked.connect(lambda :fd.open(font_sel))
        #

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
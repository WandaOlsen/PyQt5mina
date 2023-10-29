from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPlainTextEdit功能测试')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pte=QPlainTextEdit(self)
        pte.resize(300,300)
        pte.move(120,50)

        #制作一个在文本框左侧的动态行数条
        line_num_parent=QWidget(self)
        line_num_parent.resize(20,300)
        line_num_parent.move(100,50)
        line_num_parent.setStyleSheet('background-color:cyan;')

        self.line_label=QLabel(line_num_parent)
        self.line_label.move(0,5)

        line_nums='\n'.join([str(i) for i in range(1,101)])
        self.line_label.setText(line_nums)
        self.line_label.adjustSize()

        pte.updateRequest.connect(lambda rect,dy:self.line_label.move(self.line_label.x(),self.line_label.y()+dy))


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
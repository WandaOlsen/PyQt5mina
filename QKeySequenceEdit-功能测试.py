from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QKeySequenceEdit功能测试')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pte=QKeySequenceEdit(self)
        ks=QKeySequence('Ctrl+C')
        pte.setKeySequence(ks)
        #***************信号****************************
        #editingFinished()   结束编辑时发射
        #keySequenceChanged(QKeySequence keySequence) 键位序列改变时发射
        #***************信号****************************
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
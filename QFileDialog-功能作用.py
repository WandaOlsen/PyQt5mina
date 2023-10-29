from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFileDialog')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        result=QFileDialog.getOpenFileName(self,'选择一个Python文件','./',
                                            'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)','Python文件(*.py)')
        # result= QFileDialog.getOpenFileUrl(self, '选择一个Python文件')
        print(result)
        # result = QFileDialog.getSaveFileName(self, '选择一个Python文件', './',
                                             # 'All(*.*);;Images(*.png*.jpg);;Python文件(*.py)', 'Python文件(*.py)')
        # result = QFileDialog.getExistingDirectory(self, '选择一个Python文件', './')
        # result = QFileDialog.getExistingDirectoryUrl(self, '选择一个Python文件', QUrl('./'))


        # print(result)
        # def test():
        #     fd=QFileDialog(self,'选择一个文件','../','All(*.*);;Images(*.png*.jpg);;Python文件(*.py)')
        #     # fd.fileSelected.connect(lambda file:print(file))
        #     fd.setAcceptMode(QFileDialog.AcceptSave)
        #     # fd.setDefaultSuffix('txt')  #自动添加后缀名
        #     # fd.setNameFilter('Img(*.jpg *.png)')
        #     fd.open()
        #
        # btn=QPushButton(self)
        # btn.setText('按钮')
        # btn.move(100,100)
        # btn.clicked.connect(test)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QInputDialog')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # result=QInputDialog.getInt(self,'xxx1','xxx2',888,step=8)
        # result = QInputDialog.getText(self, 'xxx1', 'xxx2',echo=QLineEdit.Password) #密文形式
        # result = QInputDialog.getItem(self, 'xxx1', 'xxx2',['1','2','3'],2,True)  #2表示默认选项索引
        # print(result)
        input_d=QInputDialog(self,Qt.FramelessWindowHint)
        input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        input_d.setComboBoxItems(['1','2','3'])
        input_d.show()


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
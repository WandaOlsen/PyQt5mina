from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QComboBox')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cb=QComboBox(self)
        cb.move(100,100)
        cb.resize(200,25)
        cb.addItem(QIcon('躺平.jpg'),'str')
        cb.addItems(['ert','123','fgh'])
        cb.addItem('小学生',{'name':'卤蛋'})  #添加Data,Data不会被展示
        # model = QStandardItemModel()
        # item1 = QStandardItem('item1')
        # item2 = QStandardItem('item2')
        # item22 = QStandardItem('item22')
        # item2.appendRow(item22)
        # model.appendRow(item1)
        # model.appendRow(item2)
        # cb.setModel(model)
        # cb.setView(QTreeView(cb))
        btn=QPushButton(self)
        btn.move(200,200)
        btn.setText('测试按钮')
        btn.clicked.connect(lambda _,idx=cb.count()-1:print(cb.itemText(idx),cb.itemData(idx)))
        #clicked的参数bool型用_接受，后面使用第二个自定义的参数值

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
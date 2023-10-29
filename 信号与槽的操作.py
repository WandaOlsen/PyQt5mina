from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('$TITLE$')
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        # self.QObjectduix()
        #self.QObjectfuzi()
        self.QObjectxinhao()
    def QObject(self):
        pass

    # def QObjectduix(self):
    # 测试API
    # obj=QObject()
    # obj.setObjectName('notice')
    # print(obj.objectName())
    #
    # obj.setProperty('notice_level','error')
    # obj.setProperty('notice_level2','warning')
    # print(obj.property('notice_level'))
    # print(obj.dynamicPropertyNames())
    # with open('QObject.qss','r') as f:
    #     qApp.setStyleSheet(f.read())
    #
    # label=QLabel(self)
    # label.setText('手写的从前')
    # label.move(200,200)
    # label.setObjectName('notice')
    #
    # btn=QPushButton(self)
    # btn.setText('233')
    # btn.move(300,200)

    def QObjectfuzi(self):
        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听obj2对象被释放
        obj2.destroyed.connect(lambda: print('obj2被释放了'))
        del self.obj1
    def QObjectxinhao(self):
        # self.obj=QObject()
        # # obj.destroyed
        # # obj.objectNameChanged
        # def hs(obj):
        #     print('对象被释放了',obj)
        # self.obj.destroyed.connect(hs)
        # del self.obj
        #***********信号与槽案例**************
        btn=QPushButton(self)
        btn.setText('请点击我继续')
        def set():
            print('点我干哈')
        btn.clicked.connect(set)


        #***********信号与槽案例**************
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # win1=QWidget()
    # win1.resize(500,500)
    # win1.setStyleSheet('background-color:red;')
    # win1.show()
    #
    # win2=QWidget()
    # win2.setStyleSheet('background-color:green;')
    # win2.resize(100,100)
    # win2.setParent(win1)
    # win2.show()
    #
    # win_root = QWidget()
    # win_root.resize(500, 500)
    #
    # label = QLabel(win_root)
    # label.setText('2333333')
    # label.setParent(win_root)
    # label1 = QLabel(win_root)
    # label1.setText('456789')
    # label1.move(200, 300)
    # label1.setParent(win_root)
    #
    # btn = QPushButton(win_root)
    # btn.setText('请点击继续游戏')
    # btn.move(250, 250)
    #
    # for sub_widget in win_root.findChildren(QLabel):
    #     print(sub_widget)
    #     sub_widget.setStyleSheet('background:purple;')
    #
    # win_root.show()
    window=Window()

    window.show()
    sys.exit(app.exec_())
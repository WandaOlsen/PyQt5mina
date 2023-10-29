from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('布局管理')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        #创建三个子控件
        label1=QLabel('标签1')
        label1.setStyleSheet('background-color:cyan;')
        label2 = QLabel('标签2')
        label2.setStyleSheet('background-color:green;')
        label3 = QLabel('标签3')
        label3.setStyleSheet('background-color:red;')
        label4 = QLabel('标签4')
        label4.setStyleSheet('background-color:black;')
        # #垂直排列
        # label_width=self.width()
        # label_height=self.height()/3
        # label1.resize(int(label_width),int(label_height))
        # label2.resize(int(label_width), int(label_height))
        # label3.resize(int(label_width), int(label_height))
        # label1.move(0,0)
        # label2.move(0,int(label_height))
        # label3.move(0,int(label_height)*2)
        #
        # timer=QTimer(self)
        # timer.timeout.connect(lambda :label1.setText(label1.text()+'8899174\n'))
        # timer.start(1000)

        #布局管理器实现方式
        v_layout=QVBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        self.setLayout(v_layout)

        v_layout.replaceWidget(label2,label4)
        label2.hide()    #替换后需要将label2隐藏、删除或者添加到其他布局当中


        #布局的嵌套
        label5=QLabel('标签5')
        label5.setStyleSheet('background-color:pink;')
        label6 = QLabel('标签6')
        label6.setStyleSheet('background-color:blue;')
        label7 = QLabel('标签7')
        label7.setStyleSheet('background-color:orange;')

        h_layout=QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        #添加子控件

        v_layout.addWidget(label1)

        v_layout.addWidget(label4)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(label3)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
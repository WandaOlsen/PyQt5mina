from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('动画组的学习')
        self.resize(800,800)
        self.setup_ui()

    def setup_ui(self):
        red_btn=QPushButton('红色',self)
        green_btn=QPushButton('绿色',self)
        red_btn.resize(100,100)
        green_btn.resize(100,100)
        green_btn.move(150,150)

        red_btn.setStyleSheet('background-color:red;')
        green_btn.setStyleSheet('background-color:green;')

        #***************绿色顺时针走小圈，红色逆时针走大圈****************************
        animation=QPropertyAnimation(green_btn,b'pos',self)
        animation.setKeyValueAt(0,QPoint(150,150))
        animation.setKeyValueAt(0.25,QPoint(550,150))
        animation.setKeyValueAt(0.5,QPoint(550,550))
        animation.setKeyValueAt(0.75,QPoint(150,550))
        animation.setKeyValueAt(1,QPoint(150,150))

        animation.setDuration(7000)
        animation.setLoopCount(1)
        # animation.start()

        animation1 = QPropertyAnimation(red_btn, b'pos', self)
        animation1.setKeyValueAt(0, QPoint(0,0))
        animation1.setKeyValueAt(0.25, QPoint(0,700))
        animation1.setKeyValueAt(0.5, QPoint(700,700))
        animation1.setKeyValueAt(0.75, QPoint(700,0))
        animation1.setKeyValueAt(1, QPoint(0,0))

        animation1.setDuration(7000)
        animation1.setLoopCount(1)
        # animation1.start()
        #并行
        animation_group1=QParallelAnimationGroup(self)
        animation_group1.addAnimation(animation)
        animation_group1.addAnimation(animation1)
        #串行
        animation_group2 =QSequentialAnimationGroup(self)
        animation_group2.addAnimation(animation)
        animation_group2.addPause(5000)
        animation_group2.addAnimation(animation1)
        animation_group2.start()
        # 点红色都暂停，点绿色都开始
        red_btn.clicked.connect(lambda: animation_group1.pause())
        green_btn.clicked.connect(lambda: animation_group1.resume())
        # animation_group1.start()

        #***************绿色顺时针走小圈，红色逆时针走大圈****************************


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
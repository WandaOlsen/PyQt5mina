from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('动画学习')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton('测试按钮', self)
        btn.resize(200, 200)
        btn.move(100, 100)
        btn.setStyleSheet('background-color:cyan;')
        # 1.创建一个动画对象，并设置目标属性
        animation = QPropertyAnimation(self, b"pos", self)
        # animation=QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b'pos')

        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(1000, 600))
        #***************设置当按下按钮时动画停止，再次按下动画继续****************************
        # self.flag=True
        # def animation_operation():
        #     if self.flag:
        #         animation.pause()
        #         self.flag=False
        #     else:
        #         animation.resume()
        #         self.flag=True
        # btn.clicked.connect(animation_operation)
        def animation_operation():
            if animation.state() == QAbstractAnimation.Running:
                animation.pause()
            elif animation.state() == QAbstractAnimation.Paused:
                animation.resume()
        btn.clicked.connect(animation_operation)
        animation.finished.connect(lambda : print('结束了'))

        #***************设置当按下按钮时动画停止，再次按下动画继续****************************

        animation.setDuration(7000)
        animation.setEasingCurve(QEasingCurve.OutInBounce)
        animation.setLoopCount(-1)


        # 4.启动动画
        animation.start()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())


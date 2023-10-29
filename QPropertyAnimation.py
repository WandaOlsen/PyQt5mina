from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('动画学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton('测试按钮',self)
        btn.resize(200,200)
        btn.move(100,100)
        btn.setStyleSheet('background-color:cyan;')
        #1.创建一个动画对象，并设置目标属性
        animation=QPropertyAnimation(self,b"pos",self)
        # animation=QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b'pos')

        #2.设置属性值，开始，插值，结束
        animation.setStartValue(QPoint(0,0))
        animation.setEndValue(QPoint(1000,600))
        # animation.setStartValue(QRect(0,0,100,100))
        # animation.setEndValue(QRect(200,200,300,300))

        # # animation.setEndValue(0)

        #3.动画时长
        animation.setDuration(7000)
        animation.setEasingCurve(QEasingCurve.OutInBounce)
        animation.setLoopCount(-1)

        list=[QAbstractAnimation.Forward,QAbstractAnimation.Backward]
        animation.setDirection(list[1])

        #4.启动动画
        animation.start()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())


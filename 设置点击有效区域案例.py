#***************设置按钮内切圆为可点击区域****************************

#***************设置按钮内切圆为可点击区域****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

class Btn(QPushButton):
    def hitButton(self,point):
        #通过给定的一个点坐标，计算与圆心之间的距离
        #如果距离<半径 则认为是有效区域，返回值为True，否则返回False

        xin_x=self.width()/2
        xin_y=self.height()/2

        hit_x=point.x()
        hit_y=point.y()

        import math
        distance=math.sqrt(math.pow(hit_x-xin_x,2)+math.pow(hit_y-xin_y,2))
        # print(distance)
        if distance<self.width()/2:
            return True

        return False

    def paintEvent(self,evt):
        super().paintEvent(evt)
        painter=QPainter(self)
        painter.setPen(QPen(QColor(100,200,122),6))
        painter.drawEllipse(self.rect())

btn=Btn(window)
btn.move(100,100)
btn.setText('Python3.9.7')
btn.resize(200,200)
# btn.pressed.connect(lambda :print('1111'))
btn.setCheckable(True)
btn.toggled.connect(lambda :print('发生改变'))



window.show()
sys.exit(app.exec_())
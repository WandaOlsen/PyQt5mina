#***************鼠标移入窗口时，让label位置跟随鼠标位置，让鼠标设置为指定图标****************************
#
#***************鼠标移入窗口时，让label位置跟随鼠标位置，让鼠标设置为指定图标****************************
import sys
from PyQt5.Qt import *

class Mywindow(QWidget):
    def mouseMoveEvent(self,mv):
        print(mv.localPos())
        label=self.findChild(QLabel)
        #label.move(300,300)
        label.move(mv.localPos().x(),mv.localPos().y())
app=QApplication(sys.argv)

window=Mywindow()
window.setWindowTitle('鼠标操作')
window.resize(500,500)
window.move(200,200)
window.setMouseTracking(True)

pixmap=QPixmap('躺平.jpg').scaled(80,80)
cursor=QCursor(pixmap)
window.setCursor(cursor)

label=QLabel(window)
label.setText('Anaconda3')
label.move(100,100)
label.setStyleSheet('background-color:cyan;')


window.show()
sys.exit(app.exec_())
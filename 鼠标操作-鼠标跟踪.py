from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    def mouseMoveEvent(self,me):
        QMouseEvent
        #print('鼠标移动至',me.globalPos())    #全局
        print('鼠标移动至',me.localPos())     #局部


app=QApplication(sys.argv)

window=MyWindow()
window.setWindowTitle('Anaconda3')
window.resize(500,500)
window.setMouseTracking(True)
#print(window.hasMouseTracking())   #查看是否设置了鼠标跟踪





window.show()
sys.exit(app.exec_())
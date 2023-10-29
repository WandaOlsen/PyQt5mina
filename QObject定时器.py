from PyQt5.Qt import *
import sys

class MySQL(QObject):
    def timerEvent(self, evt):
        print(evt,'1')
app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('QObject定时器的使用')
window.resize(500,500)

obj=MySQL()
timer_id=obj.startTimer(1000)

#obj.killTimer(timer_id)

window.show()
sys.exit(app.exec_())
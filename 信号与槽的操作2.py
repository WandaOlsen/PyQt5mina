from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()

def set(title):
    #print('窗口标题变化了',title)
    #window.windowTitleChanged.disconnect()
    window.blockSignals(True)
    window.setWindowTitle('周杰伦的'+title)
    #window.windowTitleChanged.connect(set)
    window.blockSignals(False)
window.windowTitleChanged.connect(set)


window.setWindowTitle('七里香')
window.setWindowTitle('回到过去')
#window.setWindowTitle('晴天')


window.show()
sys.exit(app.exec_())
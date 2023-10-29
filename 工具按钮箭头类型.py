from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

tb=QToolButton(window)
tb.setIcon(QIcon('躺平.jpg'))
tb.setArrowType(Qt.LeftArrow)
#Qt.NoArrow
#Qt.UpArrow
#Qt.DownArrow
#Qt.LeftArrow
#Qt.RightArrow
tb1=QToolButton(window)
tb1.setText('tangping')
tb1.move(100,100)
tb1.setAutoRaise(True)      #设置自动提升使得按钮在鼠标接触时会有3D效果

window.show()
sys.exit(app.exec_())
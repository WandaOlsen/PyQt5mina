from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('文本对齐方式')
window.resize(500,500)

le=QLineEdit(window)
le.resize(300,300)
le.move(50,50)
le.setStyleSheet('background-color:cyan;')

le.setAlignment(Qt.AlignRight|Qt.AlignBottom)

#水平：Qt.AlignLeft;Qt.AlignRight;Qt.AlignHCenter;Qt.AlignJustify  #此处同左对齐
#垂直：Qt.AlignTop;Qt.AlignBottom;Qt.AlignVCenter;Qt.AlignBaseline
#Qt.AlignCenter 等同于 Qt.AlignHCenter|Qt.AlignVCenter   垂直和水平都居中

window.show()
sys.exit(app.exec_())
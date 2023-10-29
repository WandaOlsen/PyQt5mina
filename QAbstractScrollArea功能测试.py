from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('QTextEdit父类功能测试')
window.resize(500,500)

te=QTextEdit(window)

te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  #设置垂直滚动条一直都出现
#Qt.ScrollBarAlwaysOff   #始终不显示滚动条
#Qt.ScrollBarAsNeeded   #在文本内容超出长度时显示滚动条
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

#设置角落控件
btn=QPushButton(window)
btn.setIcon(QIcon('躺平.jpg'))

te.setCornerWidget(btn)

window.show()
sys.exit(app.exec_())
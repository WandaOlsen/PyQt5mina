from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

rb=QRadioButton('男',window)
rb.move(100,100)
rb2=QRadioButton('女',window)
rb2.move(100,120)           #同一个父控件内只能选中一个
rb2.setIcon(QIcon('躺平.jpg'))
rb2.setIconSize(QSize(12,12))

# rb.setShortcut('A')
# rb2.setShortcut('S')
rb3=QRadioButton('yes',window)
rb3.move(200,100)

rb4=QRadioButton('no',window)
rb4.move(200,120)

#解决方案1：创建两个父控件，放入两对按钮
window.show()
sys.exit(app.exec_())
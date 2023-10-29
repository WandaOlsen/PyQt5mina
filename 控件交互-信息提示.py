from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QMainWindow()   #懒加载   用到的时候才会创建
window.statusBar()
window.setWindowTitle('Anaconda3')
window.resize(500,500)
window.setStatusTip('Python3.9')

label=QLabel(window)
label.setText('Pycharm')
label.setStatusTip('AtomIDLE')
label.setToolTip('点击开始')

label.setToolTipDuration(2000)




window.show()
sys.exit(app.exec_())
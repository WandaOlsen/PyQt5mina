from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

btn=QCommandLinkButton('标题','描述',window)





window.show()
sys.exit(app.exec_())
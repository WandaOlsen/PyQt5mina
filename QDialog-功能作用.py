from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('QDialog')
window.resize(500,500)

d=QDialog(window)  #绑定关联窗口
d.setWindowTitle('ttt')
# d.exec_()
# d.setWindowModified(Qt.ApplicationModal)
# d.setWindowModified(Qt.WindowModal)
d.open()
d.setSizeGripEnabled(True)
# d.show()


window.show()
sys.exit(app.exec_())
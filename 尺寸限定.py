from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('最小尺寸最大尺寸限定')
#window.resize(500,500)
# window.setMinimumSize(200,200)
# window.setMaximumSize(500,500)
window.setMinimumWidth(500)
window.setMaximumHeight(800)






window.show()
sys.exit(app.exec_())
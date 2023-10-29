from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

btn=QPushButton(window)
btn.setText('按钮')
btn.setEnabled(False)
print(btn.isEnabled())




window.show()
sys.exit(app.exec_())
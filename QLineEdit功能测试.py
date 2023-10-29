from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('QLineEdit功能测试')
window.resize(500,500)

le=QLineEdit(window)
le.setText('sz')
le.insert('18')     #在光标处添加

btn=QPushButton(window)
btn.move(100,100)
btn.setText('按钮')
btn.pressed.connect(lambda :le.insert('18'))




window.show()
sys.exit(app.exec_())
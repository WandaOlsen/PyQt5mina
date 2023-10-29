from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

le=QLineEdit(window)
le.move(100,100)

le.setEchoMode(QLineEdit.NoEcho)     #不显示输入的内容但有内容
le.setEchoMode(QLineEdit.Normal)     #默认显示
le.setEchoMode(QLineEdit.Password)  #密文模式
le.setEchoMode(QLineEdit.PasswordEchoOnEdit)   #编辑的时候能看到，编辑结束变密文


window.show()
sys.exit(app.exec_())
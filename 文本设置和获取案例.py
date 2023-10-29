#***************创建一个窗口，两个文本框，一个按钮****************************
#要求：点击按钮后，将文本框A内输入的内容复制到文本框B中
#***************创建一个窗口，两个文本框，一个按钮****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

le_a=QLineEdit(window)
le_a.move(100,200)
le_b=QLineEdit(window)
le_b.move(100,300)

copy_btn=QPushButton(window)
copy_btn.setText('复制')
copy_btn.move(150,400)

def copy():
    now_text=le_a.text()         #displaytext()是指用户看到的内容
    le_b.setText(now_text)
copy_btn.pressed.connect(copy)



window.show()
sys.exit(app.exec_())
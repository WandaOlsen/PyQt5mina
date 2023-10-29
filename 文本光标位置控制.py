from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('光标测试')
window.resize(500,500)

le=QLineEdit(window)
le.move(150,150)

btn=QPushButton(window)
btn.setText('按钮')
btn.move(180,250)
def cursor_move():
    # le.cursorBackward(False,2)
    # le.cursorBackward(True, 2)       #光标向左移动，True表示移动时选中字符
    # le.cursorForward(True, 3)          #光标向右（向前）
    # le.cursorWordBackward(True)    #向左选中一个单词，以空格作为区分，空格两侧识别为一个单词
    # le.cursorWordForward(True)
    # le.home(True)          #光标自动移动至行首，True代表选中
    # le.end(False)      #光标移动至行尾
    print(le.cursorPosition())  #获取光标位置
    # le.setCursorPosition(len(le.text())/2)
    le.cursorPositionAt(QPoint(55,5))          #以文本框左上角为圆心坐标55,5处的字符前面的字符长度之和


    le.setFocus()
btn.clicked.connect(cursor_move)


window.show()
sys.exit(app.exec_())
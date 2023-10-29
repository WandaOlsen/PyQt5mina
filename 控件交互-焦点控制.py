from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self,evt):
        print(self.focusWidget())
        # self.focusNextChild()
        # self.focusPreviousChild()
        # self.focusNextPrevChild(True)  #True代表前面Next,False代表后面
        self.setTabOrder(le3,le1)
app=QApplication(sys.argv)

window=Window()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

le1=QLineEdit(window)
le1.move(50,50)

le2=QLineEdit(window)
le2.move(100,100)


le3=QLineEdit(window)
le3.move(150,150)

# le2.setFocus()
# le2.setFocusPolicy(Qt.TabFocus)  #只能通过Tab键获取
# le2.setFocusPolicy(Qt.ClickFocus)  #只能通过鼠标点击获取
# le2.setFocusPolicy(Qt.StrongFocus) #以上两种都可以
# le2.setFocusPolicy(Qt.NoFocus)  #以上两种都不可以，只能通过手动setFocus()

window.show()
sys.exit(app.exec_())
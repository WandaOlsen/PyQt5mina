from PyQt5.Qt import *
import sys


class App(QApplication):
    def notify(self,recevier,evt):
        if recevier.inherits('QPushButton') and evt.type() == QEvent.MouseButtonPress:
            print(recevier,evt)
        return super().notify(recevier,evt)

def set():
    print('按钮被点击了')

app=App(sys.argv)

window=QWidget()

btn=QPushButton(window)
btn.setText('按钮')
btn.move(200,200)
btn.pressed.connect(set)





window.show()
sys.exit(app.exec_())
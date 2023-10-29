from PyQt5.Qt import *
import sys

# class Window(QWidget):
#     def paintEvent(self,evt):
#         print(33)
#         return super().paintEvent(evt)



app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('[*]Anaconda3')
window.resize(500,500)

window.setWindowModified(True)    #将窗口设置为可编辑状态
btn=QPushButton(window)
btn.setText('按钮')
btn.setEnabled(True)
# print(btn.isEnabled())
# window.setVisible(True)




window.show()

print(btn.isHidden())
print(btn.isVisible())

sys.exit(app.exec_())
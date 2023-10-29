from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)
win=QWidget()

obj=QObject()
w=QWidget()
btn=QPushButton()
label=QLabel()

objs=[obj,w,btn,label]
for i in objs:
    print(i.isWidgetType())          #判断是否是控件类型
# for o in objs:
#     print(o.inherits('QWidget'))     #判断是否继承QWidget
for e in objs:
    print(e.inherits('QPushButton'))        #判断是否继承QPushButton

win.show()
sys.exit(app.exec_())





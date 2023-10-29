from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)
window=QWidget()


obj1=QObject()
obj2=QObject()
obj3=QObject()

obj3.setParent(obj2)
obj2.setParent(obj1)

obj1.destroyed.connect(lambda :print('1'))
obj2.destroyed.connect(lambda :print('2'))
obj3.destroyed.connect(lambda :print('3'))

obj2.deleteLater()
print(obj2)

window.show()

sys.exit(app.exec_())

#del 只是删除对象，并不会破坏原有的父子关系
#deleterLater 可以破坏对象之间的父子关系，做到删除功能
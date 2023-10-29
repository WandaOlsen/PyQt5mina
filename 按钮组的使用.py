from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('按钮组的使用')
window.resize(500,500)

r1=QRadioButton('男',window)
r2=QRadioButton('女',window)
r1.move(100,100)
r2.move(100,150)

sex_group=QButtonGroup(window)
sex_group.addButton(r1)
sex_group.addButton(r2)
# sex_group.removeButton(1)   #从组中移除按钮
r3=QRadioButton('是',window)
r4=QRadioButton('否',window)
r3.move(300,100)
r4.move(300,150)

sex_group.setId(r1,1)  #设置ID
sex_group.setExclusive(False)   #设置独占

print(sex_group.buttons())   #查看组里面的按钮


window.show()
sys.exit(app.exec_())
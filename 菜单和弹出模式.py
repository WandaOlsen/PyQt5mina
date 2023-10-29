#***************设置菜单的弹出触发方式****************************

#***************设置菜单的弹出触发方式****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

tb=QToolButton(window)
tb.setText('工具')
menu=QMenu()
menu.addAction('textboy')

tb.setMenu(menu)
# tb.setPopupMode(QToolButton.DelayedPopup)  #鼠标按住一会才会显示
# tb.setPopupMode(QToolButton.MenuButtonPopup)  #有一个专门的箭头，点击箭头才会显示
tb.setPopupMode(QToolButton.InstantPopup)  #点了按钮就显示菜单，点击信号不会发射



window.show()
sys.exit(app.exec_())
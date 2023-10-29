from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

btn=QPushButton(QIcon('躺平.jpg'),'345',window)
#***************菜单设置****************************
menu=QMenu()
open_recent_menu=QMenu('最近打开',menu)
# new_action=QAction()
# new_action.setText('新建')
# new_action.setIcon(QIcon('躺平.jpg'))

new_action=QAction(QIcon('躺平.jpg'),'新建',menu)
new_action.triggered.connect(lambda :print('新建文件'))

open_action=QAction(QIcon('躺平.jpg'),'打开',menu)
open_action.triggered.connect(lambda :print('打开文件'))

exit_action=QAction(QIcon('躺平.jpg'),'退出',menu)
exit_action.triggered.connect(lambda :print('退出'))

open_recent_menu.addAction(QAction('python PyQt5 GUI编程',open_recent_menu))
menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()         #在两个按钮之间增加分割线
menu.addAction(exit_action)
btn.setMenu(menu)
#***************菜单设置****************************
#***************扁平化****************************
btn.setFlat(True)
#设置扁平化后背景颜色不再显示

#***************扁平化****************************


window.show()
sys.exit(app.exec_())
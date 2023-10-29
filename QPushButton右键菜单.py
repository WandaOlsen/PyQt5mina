from PyQt5.Qt import *
import sys

# class Window(QWidget):
    # def contextMenuEvent(self,evt):
    #     menu = QMenu(self)
    #     open_recent_menu = QMenu('最近打开', menu)
    #     new_action = QAction(QIcon('躺平.jpg'), '新建', menu)
    #     new_action.triggered.connect(lambda: print('新建文件'))
    #
    #     open_action = QAction(QIcon('躺平.jpg'), '打开', menu)
    #     open_action.triggered.connect(lambda: print('打开文件'))
    #
    #     exit_action = QAction(QIcon('躺平.jpg'), '退出', menu)
    #     exit_action.triggered.connect(lambda: print('退出'))
    #
    #     open_recent_menu.addAction(QAction('python PyQt5 GUI编程', open_recent_menu))
    #     menu.addAction(new_action)
    #     menu.addAction(open_action)
    #     menu.addMenu(open_recent_menu)
    #     menu.addSeparator()  # 在两个按钮之间增加分割线
    #     menu.addAction(exit_action)
    #
    #     # menu.exec_(QPoint(500,500))
    #     menu.exec_(evt.globalPos())
app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

def show_menu(point):
    menu = QMenu()
    open_recent_menu = QMenu('最近打开', menu)
    new_action = QAction(QIcon('躺平.jpg'), '新建', menu)
    new_action.triggered.connect(lambda: print('新建文件'))

    open_action = QAction(QIcon('躺平.jpg'), '打开', menu)
    open_action.triggered.connect(lambda: print('打开文件'))

    exit_action = QAction(QIcon('躺平.jpg'), '退出', menu)
    exit_action.triggered.connect(lambda: print('退出'))

    open_recent_menu.addAction(QAction('python PyQt5 GUI编程', open_recent_menu))
    menu.addAction(new_action)
    menu.addAction(open_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()  # 在两个按钮之间增加分割线
    menu.addAction(exit_action)

    # menu.exec_(QPoint(500,500))
    # menu.exec_(evt.globalPos())
    dest_point=window.mapToGlobal(point)
    menu.exec_(dest_point)
window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)


window.show()
sys.exit(app.exec_())
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)


pixmap=QPixmap('躺平.jpg')
new_pixmap=pixmap.scaled(80,80)
cursor=QCursor(new_pixmap,0,0)     #改变图标生效位置，对应scaled里面的大小
window.setCursor(cursor)

#window.unsetCursor()
current_cursor=window.cursor()
#print(current_cursor.pos())
current_cursor.setPos(1696,52)

window.show()
sys.exit(app.exec_())
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)
window.setStyleSheet('background-color:black;')

icon=QIcon('躺平.jpg')
window.setWindowIcon(icon)
print(window.windowIcon())


window.setWindowOpacity(0.5)    #设置不透明度
window.setWindowState(Qt.WindowFullScreen)

window.showMaximized()


# window.show()
sys.exit(app.exec_())
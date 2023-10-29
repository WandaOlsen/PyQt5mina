from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

cb=QCheckBox('Python',window)
cb.setIcon(QIcon('躺平.jpg'))
cb.setIconSize(QSize(60,60))

cb.setTristate(True)  #设置三态  设置之后按钮有三种状态，未被选中，部分选中，全选中

# cb.setCheckState(Qt.PartiallyChecked)
# cb.setCheckState(Qt.Checked)
# cb.setCheckState(Qt.Unchecked)             #设置按钮状态

cb.stateChanged.connect(lambda state: print(state))    #三态使用stateChanged
# cb.toggled.connect(lambda isChecked: print(isChecked))    #两态使用


window.show()
sys.exit(app.exec_())
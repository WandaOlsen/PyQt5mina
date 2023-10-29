from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)

#window.setCursor(Qt.ForbiddenCursor)
#window.setCursor(Qt.ArrowCursor)
#window.setCursor(Qt.UpArrowCursor)
#window.setCursor(Qt.CrossCursor)
#window.setCursor(Qt.IBeamCursor)
#window.setCursor(Qt.WaitCursor)
#window.setCursor(Qt.BusyCursor)
# window.setCursor(Qt.PointingHandCursor)     #变为小手指
#window.setCursor(Qt.WhatsThisCursor)
#window.setCursor(Qt.SizeVerCursor)
#window.setCursor(Qt.SizeHorCursor)
#window.setCursor(Qt.SizeBDiagCursor)
#window.setCursor(Qt.SizeAllCursor)    #四箭头
#window.setCursor(Qt.SplitVCursor)
#window.setCursor(Qt.SplitHCursor)
#window.setCursor(Qt.OpenHandCursor)
#window.setCursor(Qt.ClosedHandCursor)
#window.setCursor(Qt.BlankCursor)     #区域内不显示鼠标








window.show()
sys.exit(app.exec_())
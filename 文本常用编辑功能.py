#***************文本常用的编辑功能****************************
#退格 backspace() 删除 del_() 清空 clear() 复制 copy() 剪切 cut() 粘贴 paste() 撤销undo() 重做redo()
#拖放 setDragEnabled() 设置选中文本后是否可以拖拽
#***************文本常用的编辑功能****************************
#***************文本选中****************************
#setSelection(start_pos,length) 选中指定区间的文本
#selectAll() 选中所有文本
#deselect() 取消选中已选择文本
#hasSelectedText()  是否有选中文本
#selectedText()  获取选中的文本
#selectionStart() 选中的开始位置
#selectionEnd() 选中的结束位置
#selectionLength()   选中的长度
#***************文本选中****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('编辑功能')
window.resize(500,500)

le=QLineEdit(window)
le.move(150,150)
btn=QPushButton('按钮',window)
btn.move(150,200)
def set():
    le.setSelection(0,len(le.text()))
    le.setFocus()
btn.clicked.connect(set)





window.show()
sys.exit(app.exec_())
















































































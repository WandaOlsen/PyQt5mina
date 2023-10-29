#***************创建一个按钮，初始文本为1****************************
#要求:每点击一次，则让文本数字增加1
#***************创建一个按钮，初始文本为1****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('Anaconda3')
window.resize(500,500)


#***************文本操作****************************
btn=QPushButton(window)
btn.setText(str(1))
def cao():
    number=int(btn.text())
    number=number+1
    btn.setText(str(number))
btn.clicked.connect(cao)
#***************文本操作****************************
#***************图标操作****************************
icon=QIcon('躺平.jpg')
btn.setIcon(icon)
size=QSize(50,50)
btn.setIconSize(size)
#***************图标操作****************************
#***************快捷键的设定****************************
# btn.setText('&abc')                            #设置Alt+a为快捷键
# btn.pressed.connect(lambda :print('333333'))
# btn.setShortcut('Alt+a')
#***************快捷键的设定****************************
#***************自动重复设置****************************
print(btn.autoRepeat())    #检测按钮是否设置了自动重复
btn.setAutoRepeat(True)
btn.setAutoRepeatDelay(2000)  #点击两秒后开始进入重复
btn.setAutoRepeatInterval(1000)  #系统每隔一秒检测一次按钮状态
#***************自动重复设置****************************
#***************状态设置****************************
push_button=QPushButton(window)
push_button.setText('这是QPushButton')
push_button.move(100,100)

radio_button=QRadioButton(window)
radio_button.setText('这是一个radio')
radio_button.move(100,150)

checkbox=QCheckBox(window)
checkbox.setText('这是checkbox')
checkbox.move(100,200)

push_button.setStyleSheet('QPushButton:pressed {background-color:red;}')
#把三个按钮，置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)
#设置push_button可以被选中
push_button.setCheckable(True)

radio_button.setChecked(True)
radio_button.toggle()  #对按钮状态取反


#***************状态设置****************************
#***************排他性设置****************************
for i in range(3):
    btn=QPushButton(window)
    btn.setText('btn'+str(i))
    btn.move(50*i,50*i)

    btn.setAutoExclusive(True)   #设置按钮相互排斥  单选


#***************排他性设置****************************



window.show()
sys.exit(app.exec_())
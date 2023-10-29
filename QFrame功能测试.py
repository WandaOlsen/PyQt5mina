from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('QFrame功能测试')
window.resize(500,500)

frame=QFrame(window)
frame.resize(100,100)
frame.move(100,100)
frame.setStyleSheet('background-color:cyan;')

#***************功能测试****************************
#setFrameShape()
#QFrame.NoFrame什么都没画
#QFrame.Box围绕其内容绘制一个框
#QFrame.Panel绘制一个面板，使得内容显得凸起或凹陷
#QFrame.HLine绘制一条没有框架的水平线（用作分隔符）
#QFrame.VLine绘制一条无框架的垂直线（用作分隔符）
#QFrame.StyledPanel 绘制一个矩形面板，其外观取决于当前的GUI样式

#setFrameShadow()
#QFrame.Plain   框架和内容与周围环境呈现水平；（没有任何3D效果）
#QFrame.Raised  框架和内容出现凸起；使用当前颜色组的浅色和深色绘制3D凸起线
#QFrame.Sunken  框架和内容出现凹陷；使用当前颜色组的浅色和深色绘制凹陷线

#外线宽度 setLineWidth(int width)  lineWidth()
#中线宽度  setMidLineWidth(int width)  midLineWidth()
#总宽度  frameWidth()
#通过控制线宽，来达到不同的组合效果

#setFrameStyle(int style)  #框架样式
#setFrameRect(QRect)  #框架矩形
#***************功能测试****************************
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShadow(QFrame.Raised)

frame.setFrameStyle(QFrame.Box|QFrame.Raised)
frame.setFrameRect(QRect(20,20,60,60))
frame.setLineWidth(6)
frame.setMidLineWidth(12)


window.show()
sys.exit(app.exec_())
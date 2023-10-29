#***************QRubberBand****************************
#在一个空白窗口内，展示多个复选框控件，通过橡皮筋实现批量选择与取消选中效果
#***************QRubberBand****************************
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QRubberBand')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 添加子控件，复选框
        for i in range(0,30):
            cb=QCheckBox(self)
            cb.setText('{}'.format(i))
            cb.move(i%4*50,i//4*60)
        self.rb = QRubberBand(QRubberBand.Rectangle, self)
    def mousePressEvent(self,evt):
        #鼠标按下，创建一个橡皮筋选中控件

        #尺寸大小：鼠标点击的位置点，00
        self.origin_pos=evt.pos()
        self.rb.setGeometry(QRect(evt.pos(),QSize()))
        #展示橡皮筋控件
        self.rb.show()


    def mouseMoveEvent(self,evt):
        #调整橡皮筋选中控件的位置以及尺寸
        self.rb.setGeometry(QRect(self.origin_pos,evt.pos()).normalized())  #如果产生负数，则会将两点坐标交换

    def mouseReleaseEvent(self,evt):
        #获取橡皮筋尺寸控件范围
        rect=self.rb.geometry()
        #遍历所有的子控件，查看，哪些子控件在区域范围
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits('QCheckBox'):
                child.toggle()
        self.rb.hide()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
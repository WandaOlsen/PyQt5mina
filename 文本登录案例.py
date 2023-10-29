#***************创建一个窗口，添加两个文本框一个按钮****************************
#要求：一个用作账号，另一个用作密码；点击登录按钮后获取账号和密码信息；
#进行对比账号密码信息：正确账号209084063，正确密码：123890；如果账号错误则清空账号框和密码框，密码错误则清空密码框。
#***************创建一个窗口，添加两个文本框一个按钮****************************


from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit-登录案例')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        self.zhanghao=QLineEdit(self)
        self.mima=QLineEdit(self)
        self.mima.setEchoMode(QLineEdit.Password)
        self.zhanghao.setFocusPolicy(Qt.StrongFocus)
        self.mima.setFocusPolicy(Qt.StrongFocus)
        self.login_btn=QPushButton(self)

        self.login_btn.setText('登录')
        self.login_btn.clicked.connect(self.put_chao)
        self.zhanghao.setPlaceholderText('请输入账号')     #占位提示字符串
        self.mima.setPlaceholderText('请输入密码')         #设置占位提示字符串
        #设置密码文本框自动显示清空按钮
        self.mima.setClearButtonEnabled(True)
        #添加自定义操作
        #***************添加自定义操作****************************
        action = QAction(self.mima)
        action.setIcon(QIcon('躺平.jpg'))

        def change():
            if self.mima.echoMode() == QLineEdit.Normal:
                self.mima.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon('躺平.jpg'))
            else:
                self.mima.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon('铜锣烧.png'))

        action.triggered.connect(change)
        self.mima.addAction(action, QLineEdit.TrailingPosition)
        #***************添加自定义操作****************************


        self.label1=QLabel(self)
        self.label1.setText('账号错误！')
        self.label2=QLabel(self)
        self.label2.setText('密码错误！')
        self.label3=QLabel(self)
        self.label3.setText('登录成功！')
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        #***************自动补全联想****************************
        completer=QCompleter(['209084063','209084064','209084065','209084066'])
        self.zhanghao.setCompleter(completer)
        #***************自动补全联想****************************
        #***************最大长度限制 只读限制****************************
        self.mima.setMaxLength(6)
        # self.zhanghao.setText('209084063')
        # self.zhanghao.setReadOnly(True)
        #***************最大长度限制 只读限制****************************

    def put_chao(self):
        account=self.zhanghao.text()
        password=self.mima.text()
        if account != '209084063':
            self.label1.setVisible(True)
            self.zhanghao.setText('')
            self.mima.setText('')
            self.zhanghao.setFocus()
            return None              #利用return None 提前退出函数实现判断
        if password != '123890':
            self.label1.setVisible(False)
            self.label2.setVisible(True)
            self.mima.setText('')
            self.mima.setFocus()
            return None
        self.label2.setVisible(False)
        self.label1.setVisible(False)
        self.label3.setVisible(True)




        # if account=='209084063':
        #     if password=='123890':
        #         print('登录成功')
        #     else:
        #         print('密码错误')
        #         self.mima.setText('')
        #         self.mima.setFocus()
        # else:
        #     print('账号错误')
        #     self.zhanghao.setText('')
        #     self.mima.setText('')
        #     self.zhanghao.setFocus()

    def resizeEvent(self,evt):
        width_x = 150
        height_y = 40
        margin = 80
        chang=120
        kuang=40
        self.zhanghao.resize(width_x, height_y)
        self.mima.resize(width_x, height_y)
        self.login_btn.resize(width_x, height_y)
        self.label1.resize(chang,kuang)
        self.label2.resize(chang,kuang)
        self.label3.resize(chang,kuang)

        x = (self.width() - width_x) / 2
        y = self.height() / 5
        self.zhanghao.move(x, y)
        self.label1.move(x,y+margin/2)
        self.mima.move(x, y + margin)
        self.label2.move(x,y+1.5*margin)
        self.login_btn.move(x, y + margin + margin)
        self.label3.move(x,y+2.5*margin)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())


#***************内容补充****************************
#1.设置当账号和密码框有一个没有内容时，登录按钮禁用
#2.在账号和密码框下面设置提示框，当输入有错误后弹出提示
#***************内容补充****************************
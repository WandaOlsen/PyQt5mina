#***************掩码含义****************************
#掩码可以指定固定位置的固定数据类型，达到一个格式上的限制
#例如：座机号码：四位区号-七位电话；IP地址：xxx.xxx.xxx.xxx
#掩码由一串掩码字符和分隔符组成
#***************掩码含义****************************
from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle('掩码测试')
window.resize(500,500)

le=QLineEdit(window)
le.move(150,150)
#设置掩码
#总共输入5位   左边2位(必须是大写字母) - 右边2位(必须是一个数字)
le.setInputMask('>AA-99;#')
#>:以下所有字母字符均为大写字母
#<:以下所有字母字符均为小写字母
# ;#表示空白时候用#填充
#A表示26个之中的一个字母
#9表示0-9之间的一个数字


window.show()
sys.exit(app.exec_())
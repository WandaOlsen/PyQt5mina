from PyQt5.Qt import *

class AgeVadidtor(QValidator):
    def validate(self,input_str,pos_int):
        print(input_str,pos_int)
        try:
            if 18<=int(input_str)<=180:
                return (QValidator.Acceptable,input_str,pos_int)
            elif 1<=int(input_str)<=17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            if len(input_str)==0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid,input_str,pos_int)
    def fixup(self,p_str):
        print(p_str)
        try:
            if int(p_str)<18:
                return '18'
            return '180'
        except:
            return '18'
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('验证器的使用')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        le=QLineEdit(self)
        le.move(100,100)
        vc=AgeVadidtor()

        le.setValidator(vc)

        le1=QLineEdit(self)
        le1.move(100,200)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
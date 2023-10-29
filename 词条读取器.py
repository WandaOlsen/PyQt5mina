from PyQt5.Qt import *
QSerialPort
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('词条读取器')
        self.resize(500,500)
        self.setup_ui()
        self.Style_Sheet()

    def setup_ui(self):
        label1=QLabel('0',self)
        label1.move(100,100)
        label1.resize(100,100)
        label1.setObjectName('l1')


        label2=QLabel(self)
        label2.resize(400,30)
        label2.setStyleSheet('background-color:cyan;')
        label2.move(100,200)
        with open('../resource/七里香.txt',encoding='utf-8') as f:
            content=f.read().splitlines()

        label2.setText(content[0])
        label2.setObjectName('l2')

        def test():
            current=label1.text()
            now=int(current)+1
            label1.setText(str(now))
            label2.setText(content[now])
            if now==33:
                label1.setText('0')
                label2.setText(content[0])
        timer=QTimer(self)
        timer.timeout.connect(test)
        timer.start(1000)



    def Style_Sheet(self):
        self.setStyleSheet("""
            QLabel#l1 {
                font-family:宋体;
                font-size:60px;
                
            }
            QLabel#l2{
                font-family:宋体;
                font-size:30px;
            }
        """)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())




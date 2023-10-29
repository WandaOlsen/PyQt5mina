from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QCalendarWidget')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cw=QCalendarWidget(self)
        cw.setMinimumDate(QDate(1990,1,1))
        cw.setMaximumDate(QDate(2024,1,1))
        cw.setDateRange(QDate(1990,1,1),QDate(2025,10,10))

        cw.setDateEditAcceptDelay(3000)
        print(cw.selectedDate())

        tcf=QTextCharFormat()
        tcf.setFontFamily('宋体')

        cw.setHeaderTextFormat(tcf)
        t_tcf=QTextCharFormat()
        t_tcf.setFontPointSize(20)
        t_tcf.setToolTip('这是星期二')
        cw.setWeekdayTextFormat(Qt.Tuesday,t_tcf)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())





















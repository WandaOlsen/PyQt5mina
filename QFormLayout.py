from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QFormLayout')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # name_label=QLabel('姓名:')
        age_label=QLabel('年龄:')
        name_le=QLineEdit()
        age_sb=QSpinBox()
        btn=QPushButton('提交')
        sex_label=QLabel('性别')
        male_rb=QRadioButton('男')
        female_rb=QRadioButton('女')
        h_layout=QHBoxLayout()
        h_layout.addWidget(sex_label)
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)


        #创建表单布局管理器
        layout=QFormLayout()

        #把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        #把需要布局的子控件交给布局管理器进行布局
        layout.addRow('姓名:',name_le)
        layout.addRow(h_layout)
        layout.addRow(age_label,age_sb)
        layout.addRow(btn)


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())
#***************给定城市数据，实现两级联动效果****************************

#***************给定城市数据，实现两级联动效果****************************
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QComboBox案例')
        self.resize(500,500)
        self.city_dic={
            '北京':{
                '东城':'001',
                '西城':'002',
                '朝阳':'003',
                '丰台':'004'
            },
            '上海':{
                '黄埔':'005',
                '徐汇':'006',
                '长宁':'007',
                '静安':'008',
                '松江':'009'
            },
            '广东':{
                '广州':'010',
                '深圳':'011',
                '湛江':'012',
                '佛山':'013'
            }
        }
        self.setup_ui()

    def setup_ui(self):
        #创建两个下拉列表控件
        pro=QComboBox(self)
        city=QComboBox(self)
        pro.move(100,100)
        city.move(200,100)
        self.pro=pro
        self.city=city
        #展示数据到第一个下拉选择控件当中

        #监听省下拉列表里面的当前值发生改变的信号
        pro.currentIndexChanged[str].connect(self.pro_changed)
        # self.pro_changed(pro.currentText())
        city.currentIndexChanged[int].connect(self.city_changed)
        # self.city_changed(city.currentIndex())
        pro.addItems(self.city_dic.keys())
    def pro_changed(self,pro_name):
        # print(pro_name)
        #根据省的名称，到字典里面，获取对应的城市字典
        citys=self.city_dic[pro_name]
        # print(citys)
        self.city.blockSignals(True)  #临时阻断信号
        self.city.clear()
        self.city.blockSignals(False) #清空后再恢复连接
        # self.city.addItems(citys.keys())
        for key,val in citys.items():
            self.city.addItem(key,val)
    def city_changed(self,city_name):
        # print(city_name)
        print(self.city.itemData(city_name))


if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())


























import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('第一个窗体')  # 标题

# 获取屏幕尺寸计算参数，使窗口显示再屏幕中央
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 650
height = 500
# window_size = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
window_size = f'{width}x{height}+{round((screen_width - width) / 2)}+{round((screen_height - height) / 2)}'  # round去掉小数
window.geometry(window_size)  # 窗口大小
# window.resizable(width=False,height=False) #设置窗体是否可用改变大小;默认可用改变
# 进入等待与处理窗口（监控每个组件，当组件发生变化或触发事件时，会立即更新窗口）
print(window_size)
window.mainloop()
# from tkinter import *
#
# win=Tk()
# win.geometry('650x500')
#
# win.mainloop()
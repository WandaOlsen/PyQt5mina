from tkinter import *
import os

def set():
    os.system(r'python 绘制波动函数.py')
def get():
    os.system(r'python 观察波包变化.py')

root=Tk()
root.geometry('200x150')
label=Label(root,text='光学仿真',bd=3,fg='purple')
label.pack()
button1=Button(root,text='绘制波动函数',bd=3,fg='red',command=set)
button1.pack(side=LEFT)
button2=Button(root,text='观察波包变化',bd=3,fg='red',command=get)
button2.pack(side=RIGHT)

root.mainloop()

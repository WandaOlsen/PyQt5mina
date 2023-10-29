from tkinter import *
import os

def set():
    os.system(r'python 定时器案例1.py')
win=Tk()
win_size=f'{200}x{150}+{470}+{200}'
win.geometry(win_size)

btn=Button(win,text='点击开始计时',bd=3,fg='red',font=30,command=lambda :[win.destroy(),set()])
btn.pack(padx=5,pady=5)

win.title('控制按钮')
win.mainloop()

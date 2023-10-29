from tkinter import *
import os

win=Tk()

win_size=f'{750}x{500}+{443}+{182}'
win.geometry(win_size)

label=Label(win,text='新年快乐',bd=5,fg='red',width=600,height=4000)


label.pack()

win.mainloop()
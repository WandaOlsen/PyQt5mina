# import turtle
# t = turtle.Turtle()
# t.color("yellow")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(0, -50)
# t.pendown()
# t.color("green")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(-50, -100)
# t.pendown()
# t.color("orange")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(50, -100)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(-100, -150)
# t.pendown()
# t.color("purple")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(100, -150)
# t.pendown()
# t.color("blue")
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# turtle.done()
# from PyQt5.Qt import *
# import matplotlib.pyplot as plt
#
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('')
#         self.resize(500,500)
#         self.setup_ui()
#
#     def setup_ui(self):
#         fig = plt.figure()
#         # 画五角星
#         x = [0, 0.5, 1, 0.5, 0]
#         y = [0.5, 1, 0.5, 0, 0.5]
#         plt.plot(x, y)
#         # 将画布添加到QWidget
#         self.addFigure(fig)
#
#
# if __name__ == '__main__':
#     import sys
#     app=QApplication(sys.argv)
#
#     window=Window()
#     window.show()
#
#     sys.exit(app.exec_())
x=input(32)
y=input(17)
print(type(x))


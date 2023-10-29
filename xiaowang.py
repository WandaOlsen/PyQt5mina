import random

n=random.randint(1,30)

while True:
    for i in range(3):
        c = input('请猜一个数：')
        if int(c) == n:
            print('你猜对了')
            exit()
        else:
            print('你猜错了')
    d=input('是否想继续？Yy/Nn')
    if d=='N' or d=='n':
        break



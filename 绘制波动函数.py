import numpy as np
import matplotlib.pyplot as plt

def set_y0(x,k,L):
    y=np.zeros_like(x)
    y[x<L]=np.sin(k*x[x<L])*np.sin(np.abs(x[x<L]*np.pi/L))
    return y
if __name__ == '__main__':
    x=np.linspace(0,10,1000)
    k=np.pi*2/1.064
    L=5
    y=set_y0(x,k,L)

    plt.plot(x,y)
    plt.show()
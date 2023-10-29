import numpy as np
import matplotlib.pyplot as plt

def set_y0(x,k,L):
    y=np.zeros_like(x)
    y[x<L]=np.sin(np.abs(x[x<L]*np.pi/L))*np.sin(k*x[x<L])
    return y

def wave1d(x,t,k,L):
    dx=x[1]-x[0]
    dt=t[1]-t[0]
    d2=(dt/dx)**2
    y=np.zeros([len(t),len(x)])
    y[0,:]=set_y0(x,k,L)
    y[1,:]=set_y0(x-dt,k,L)
    for n in range(2,len(t)):
        y[n]=2*y[n-1]-y[n-2]-d2*2*y[n-1]
        y[n,1:]+=d2*y[n-1,:-1]
        y[n,:-1]+=d2*y[n-1,1:]
        y[n,0]=0
        y[n,-1]=0
    return y

import matplotlib.animation as animation

def drawGif(t,x,ys,mark='time='):
    tAxis=np.linspace(0,len(t)-1,100).astype(int)
    fig=plt.figure()
    ax=fig.add_subplot(111,xlim=(0,10),ylim=(-1.5,1.5))
    ax.grid()
    line,=ax.plot([],[],lw=0.2)
    time_text=ax.text(0.1,0.9,'',transform=ax.transAxes)
    def init():
        line.set_data([],[])
        time_text.set_text("")
        return line,time_text
    def animate(i):
        y=ys[i]
        line.set_data(x,y)
        time_text.set_text(mark+str(t[i]))
        return line,time_text
    ani=animation.FuncAnimation(fig,animate,tAxis,interval=200,init_func=init)
    ani.save('wave.gif',writer='imagemagick')
    plt.show()

if __name__ == '__main__':
    x=np.linspace(0,10,1000)
    t=np.linspace(0,12,2041)
    k=np.pi*2/1.064
    L=5
    y=wave1d(x,t,k,L)
    drawGif(t,x,y)







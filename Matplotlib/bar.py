import matplotlib.pyplot as plt
import numpy as np

n = 12
x= np.arange(n)
y1 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)
y2 = (1-x/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(x,+y1,facecolor='#9999ff',edgecolor='white')

plt.bar(x,-y2,facecolor='#ff9999',edgecolor='white')

for X,Y in zip(x,y1):
    plt.text(X+0.4,Y+0.05,'%.2f' % Y,ha='center',va='bottom')

for X,Y in zip(x,-y2):
    plt.text(X-0.4,Y-0.05,'%.2f' % Y,ha='center',va='top')

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()
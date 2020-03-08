import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()

x = [1,2,3,4,5,6,7]
y = [1,3,4,5,6,7,8]

left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')


plt.show()
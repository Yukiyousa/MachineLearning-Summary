import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
ax1.plot([1,2],[1,2])
ax1.set_title('axis1')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax2.set_title('axis2')
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1))

plt.show()
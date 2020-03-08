import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x ** 2
y2 = 2 * x + 1

# plt.figure()
# plt.title("y=x^2")
# plt.plot(x, y1)

plt.figure(figsize=(8, 5))
plt.title("y=2x+1")

# 两条图线设置
l1,=plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--',label = 'up')
l2,=plt.plot(x, y1, color='green', linewidth = 1.5, label= 'down')
plt.legend(handles=[l1,l2,],labels=['y=2x+1','y=x^2'],loc='best') # 也可默认legend()


plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel("X")
plt.ylabel("Y")

# 设置坐标轴标注
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3, ], [r'$really\ bad$', r'$bad\ $', r'$normal$', r'$good\ \alpha$', r'$really\ good$'])
ax = plt.gca()

# 设置坐标轴位置
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()





plt.figure(figsize=(8, 5))
plt.title("标注")

# 两条图线设置
l1,=plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--',label = 'up')
#l2,=plt.plot(x, y1, color='green', linewidth = 1.5, label= 'down')
plt.legend(handles=[l1,],labels=['y=2x+1'],loc='best') # 也可默认legend()


plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel("X")
plt.ylabel("Y")

# 设置坐标轴标注
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3, ], [r'$really\ bad$', r'$bad\ $', r'$normal$', r'$good\ \alpha$', r'$really\ good$'])
ax = plt.gca()

# 设置坐标轴位置
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
x0 = 0.5
y0 = 2
plt.scatter(x0,y0,s=50,color='blue')
plt.plot([x0,x0],[x0,y0],'b--',lw=3)

# 标注方法1
#plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0),xycoords='data', xytext=(+30,-30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# 标注方法2
# plt.text(-0.75, 2, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 9, 'color': 'r'})

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='r', edgecolor='None', alpha=0.1))
plt.show()

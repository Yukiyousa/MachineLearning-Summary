import numpy as np

a = np.arange(4)
b = a # b指向a
print(a)
a[0] = 4
print('b= ',b)
print('a= %s \n' % str(a))
b1 = a.copy()
a[0] = 3
print(b1)
print(a)
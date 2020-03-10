import numpy as np

a = np.array([1, 1, 1]).reshape(3, 1)
b = np.array([2, 2, 2]).reshape(3, 1)

c = np.vstack((a, b))
d = np.hstack((a, b))

a1 = np.arange(3, 15).reshape(3, 4)
print(a1)
b1 = np.split(a1, 3, axis=0)
print(b1)
print(np.array_split(a1,3,axis=1))

multi = np.concatenate((a, b), axis=1)
print(multi)
# print(a)
# print(c)
# print(d)

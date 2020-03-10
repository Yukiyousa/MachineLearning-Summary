import numpy as np

a = np.arange(2,11).reshape((3,3))
b = np.arange(19,10,-1).reshape((3,3))

print(a*b)
print(a.dot(b))

print(np.argmin(a))
print(np.argmax(a))
print(a.mean())

print(np.sort(a,axis=1))
print(np.argsort(a))
print(np.transpose(a))
print(a.T)
print(np.clip(a,5,9))
print(a.mean(axis=1))

asw = np.arange(3,15).reshape(3,4)
print(asw)
# print(asw[2])
# print(asw[:,1])

for row in asw:
    print(row)
for item in asw.flat:
    print(item)
import numpy as np

array = np.array([[1,2,3],[2,3,4]])
zero = np.zeros((3,4),dtype=np.int)
print(zero)
one = np.ones((3,4),dtype=np.int)
print(one)
a = np.array([2,23,3],dtype=np.int)
print(a.dtype)

range = np.arange(10,20,2)
print(range)
range_shape = np.arange(12).reshape((3,4))
print(range_shape)

line = np.linspace(1,20,20)
print(line)


print('number of dim',array.ndim)
print('shape:',array.shape)
print(array.size)
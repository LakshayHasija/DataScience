import numpy as np
a = np.array([1, 2, 3])
print(a)
b = np.array([[2, 0, 8, 6, 0], [2, 8, 0, 0, 6]])
# dimensions -- a.ndim -- no of dimensions -- 1(of a)
print(b.ndim)
# get shape -- a.shape -- 3
print(b.shape)
# get type -- int32 / int 16 / int 8
print(b.dtype)
# get size -- bits size(32-4/16-2)
print(b.itemsize)
# get total size -- size + item size (a.size + a.itemsize)
print(a.nbytes)
print(a.size)
print(a.itemsize)

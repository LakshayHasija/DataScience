import numpy as np

a = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])
print(a)
# get specific element -- a[row,column]
print(a[0, 2])
# replace
a[0, 0] = 10
print(a)

import numpy as np
# all maths functions can be used in numpy --  +  -  /  *  **(square)  np.sin(trigo)
a = np.array([1, 2, 3, 4])
print(np.sin(a))
print(a+2)
b = ([1, 2, 1, 2])
print(a+b)

# linear algebra

# matrix mult
c = np.full((2, 3), 5)
d = np.full((3, 2), 3)
e = np.matmul(c, d)
print(e)

# find the determinant
f = np.identity(5)
print(np.linalg.det(f))

# statistics
stats = np.array([[1, 2, 3], [4, 5, 6]])

print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

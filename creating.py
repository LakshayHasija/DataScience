import numpy as np

# all 0 matrix
a = np.zeros((2, 2, 2))
print(a)
# all ones matrix
b = np.ones((2, 3, 3))
print(b)
# any number --np.full((2,2),no you want)
c = np.full((3, 3), 5)
print(c)
# full like (size) of a , any no
d = np.full_like(a, 4)
print(d)
# random decimal matrix
e = np.random.rand(4, 2)
print(e)
# random integer matrix -- range of integers , size
f = np.random.randint(0, 5, size=(2, 2))
print(f)
# identity matrix -- size
g = np.identity(5)
print(g)
# repeat an array
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)
# creating
# [1,1,1,1,1]
# [1,0,0,0,1]
# [1,0,9,0,1]
# [1,0,0,0,1]
# [1,1,1,1,1]
output = np.ones((5, 5))
print(output)
z = np.zeros((3, 3))
z[1, 1] = 9
print(z)
output[1:-1, 1:-1] = z
print(output)
# copying array -- b=a (wrong) -- b=a.copy() (right)

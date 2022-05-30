import numpy as np

# reshape
a = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
b = np.reshape(a, (2, 2, 2))
print(b)

# v-stack

c = np.ones((2, 3))
d = np.zeros((4, 3))
print(np.vstack((c, d)))
e = np.ones((4, 2))
print(np.hstack((e, d)))

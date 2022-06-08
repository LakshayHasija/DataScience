import numpy as np
import pandas as pd
df = pd.DataFrame([[4, 7, 10],
                   [6, 8, 2],
                   [1, 3, 4],
                   [2, 10, 5]])
print(df.loc[1:4])
x = np.array([[1, 2], [3, 4], [2, 2], [9, 6]])
print(np.sum(x, axis=1))

# load misc data
#a = np.genfromtxt('data.txt', delimiter=',')
#a = a.astype('int32')
# print(a)
#print(a > 5)

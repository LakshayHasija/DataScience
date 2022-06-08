import numpy as np
import matplotlib.pyplot as plt
dataset = np.array([20, 18, 10, 11, 14, 15, 13, 18, 102, 22, 19,
                   14, 17, 201, 17, 19, 20, 25, 24, 23, 25, 17, 18, 19, 10, 18, 20, 22, 23, 24, 18, 20, 22, 23, 24, 18, 20, 22, 23, 24, 18, 20, 22, 23, 24, 22, 21, 27, 25, 13, 15, 26])

# #METHOD 1
# #finding outliers using z-score
# # z-score = x-mean/std--threshold
# outliers = []


# def detect_outliers(data):
#     threshold = 3
#     mean = np.mean(data)
#     std = np.std(data)
#     for i in data:
#         z_score = (i-mean)/std
#         if np.abs(z_score) > threshold:
#             outliers.append(i)
#     return outliers


# outliers_pt = detect_outliers(dataset)
# print(outliers_pt)


# METHOD-2
# Finding outliers using iqr
dataset = sorted(dataset)
q1, q3 = np.percentile(dataset, [25, 75])
print(q1, q3)
iqr = q3-q1
print(iqr)
lbv = q1-(iqr*1.5)
hbv = q3+(iqr*1.5)
print(lbv, hbv)
outliers = []
for i in dataset:
    if i > hbv or i < lbv:
        outliers.append(i)
print(outliers)

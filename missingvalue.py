import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')

# print(train.head())
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Pclass', data=train)
plt.show()

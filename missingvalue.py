import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')

# print(train.head())
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

# sns.set_style('whitegrid')
# sns.countplot(x='Survived', hue='Pclass', data=train)
# plt.show()

# sns.histplot(train['Age'].dropna(), kde=False, color='darkred', bins=40)
# plt.show()

sns.set_style('whitegrid')
sns.boxplot(x='Pclass', y='Age', data=train)
# plt.show()


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age


train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)
train.drop('Cabin', axis=1, inplace=True)
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Define random seed
RSEED = 0

# define figure size
plt.rcParams['figure.figsize'] = (10, 7)

df = pd.read_csv('data/winequality-white.csv',sep=";")
print(df.head(2))
print(df.info())

# define features and target
features = df.columns.tolist()
features.remove('quality')
X = df[features]

ax = sns.heatmap(df.corr(), annot=True)
plt.show()


import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
data = pd.read_csv('score.csv')
X = data.iloc[:, 0].values
Y = data.iloc[:, 1].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 33)

plt.scatter(X_train, Y_train, color = 'red')
regressor = LinearRegression()
pre = regressor.fit(X_train.reshape(-1,1), Y_train.reshape(-1,1))  # new version data must be 2 dimensions
plt.plot(X_train, pre.predict(X_train.reshape(-1,1)))
plt.show()
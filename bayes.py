import pandas as pd
import numpy as np
dataset = pd.read_csv('bayes.csv')
from sklearn.preprocessing import LabelEncoder
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 2].values
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])


def predict(xx):
    xx[1] = labelencoder.transform(np.array([xx[1]]))
    xx = np.array([xx[0], float(xx[1])])
    y1 = 0
    y_1 = 0
    x1 = 0
    x2 = 0
    x1_1 = 0
    x2_1 = 0
    for i in range(len(Y)):
        if Y[i] == 1:
            y1 += 1
            if xx[0] == X[i, 0]:
                x1 = x1 + 1
            if xx[1] == X[i, 1]:
                x2 += 1
        else:
            y_1 += 1
            if xx[0] == X[i, 0]:
                x1_1 = x1_1 + 1
            if xx[1] == X[i, 1]:
                x2_1 += 1
    yy_1 = y1 / len(Y) * (x1/y1)*(x2/y1)
    yy_2 = y_1 / len(Y) * (x1_1 / y_1) * (x2_1 / y_1)
    if yy_1 > yy_2:
        return 1
    else:
        return -1



a = predict([2, 'S'])
print(a)





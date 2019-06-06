import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
dataset = pd.read_csv('credit.csv', encoding="gbk")
X = dataset.iloc[:, :-1].values   # 这样才能是数值
Y = dataset.iloc[:, -1].values
XP =  list(dataset.iloc[:, :-1])
XM = dataset.iloc[:, :-1].values.copy()
YM = dataset.iloc[:, -1].values.copy()
labelencoder = LabelEncoder()
for i in range(0, 4):
    X[:, i] = labelencoder.fit_transform(X[:, i])

Y = labelencoder.fit_transform(Y)
XMM = {}
YPP = {}

for i in range(len(X[0])):
    XMM[i] = {}
    for j in range(len(Y)):
        if X[j, i] not in XMM[i].keys():
            XMM[i][X[j, i]] = XM[j, i]
for j in range(len(Y)):
    if Y[j] not in YPP.keys():
        YPP[Y[j]] = YM[j]








def cal_ent(yy):
    length = len(yy)
    feature = {}
    ent = 0
    for i in range(length):  # 如何求得一个数组中不同特征的个数
        if yy[i] not in feature.keys():
            feature[yy[i]] = 1
        else:
            feature[yy[i]] += 1
    for k in feature.keys():   # 如何遍历一个字典
        p = feature[k] / length
        ent += -p * np.log2(p)
    return ent


def cal_gain(X, Y, feature):
    D = cal_ent(Y)
    length = len(Y)
    x_feature = {}
    y = []
    t = 0
    y_feature = {}
    gain = 0
    for i in range(length):
        if X[i, feature] not in x_feature.keys():
            x_feature[X[i, feature]] = 1
            t = t + 1
            y_feature[X[i, feature]] = [Y[i]]

        else:
            x_feature[X[i, feature]] += 1
            y_feature[X[i, feature]].append(Y[i])

    for fea in y_feature.keys():
        ent1 = cal_ent(np.array(y_feature[fea]))
        pp = x_feature[fea] / length
        gain += pp * ent1

    p = D - gain
    return p, x_feature


def split_data(X, Y, feature):
    m = len(Y)
    a = set(X[:, feature])
    tt = {}
    yy = {}
    for t in a:
        tt[t] = []
        yy[t] = []
    for i in range(m):
        for value in a:
            if X[i, feature] == value:
                aa = X[i, :feature]
                bb = X[i, feature+1:]
                tt[value].append(list(np.hstack((aa, bb))))
                yy[value].append(Y[i])

    return tt, yy


def creat_tree(X, Y):
    n = len(X[0])
    m = len(Y)
    if len(set(Y)) == 1:
        return YPP[Y[0]]
    min_gain = 0

    for i in range(n):
        gain_inf, x_feature = cal_gain(X, Y, i)
        if gain_inf > min_gain:
            min_gain = gain_inf
            maxi = i
    tree = {XP[maxi]:{}}
    tt, yy = split_data(X, Y, maxi)
    for key in tt.keys():
        tree[XP[maxi]][XMM[maxi][key]] = creat_tree(np.array(tt[key]) , np.array(yy[key]))
    return tree     # 递归函数的返回值很重要，没有返回值的化等于没有递归



tree = creat_tree(X, Y) 
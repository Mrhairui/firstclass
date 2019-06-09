import numpy as np
import matplotlib.pyplot as plt
# dataset = pd.read_csv('testSet.txt') # 不能用read_csv因为CSV是以逗号分隔的，一般的文本文档是以制表符分隔的，所以读入内容是错的
fr = open('testSet.txt')
X = []
Y = []
for line in fr.readlines():
    linearr = line.strip().split('\t')
    a = [float(i) for i in linearr[0: -1]]
    X.append(a)
    Y.append(float(linearr[-1]))

xx1 = []
xx2 = []
for i in range(len(Y)):
    if Y[i] == 1:
        xx1.append(X[i])
    else:
        xx2.append(X[i])
xx1 = np.array(xx1)
xx2 = np.array(xx2)
plt.scatter(xx1[:, 0], xx1[:, 1], color = 'red')
plt.scatter(xx2[:, 0], xx2[:, 1], color = 'blue')


X = np.mat(X)
Y = np.mat(Y).transpose()
C = 5
m, n = np.shape(X)
alpha = np.mat(np.zeros((m, 1)))
b = 0
maxiter = 100
toler = 0.001
iter = 0

def selectj(i, m):
    j = i
    while(j == i):
        j = int(np.random.uniform(0, m))
    return j

def clipalpha(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj


while (iter < maxiter):
    for i in range(m):
        fxi = float(np.multiply(alpha, Y).T * X * X[i, :].T) + b  # 转化为矩阵后，*代表点乘， multiply代表对应元素相乘
        ei = fxi - Y[i, 0]
        if (ei * Y[i, 0] > toler) and (alpha[i, 0]>0) or (ei * Y[i, 0] < toler) and (alpha[i, 0]<C):
            j = selectj(i, m)
            fxj = float(np.multiply(alpha, Y).T * X * X[j, :].T) + b
            ej = fxj - Y[j, 0]
            alphaiold = alpha[i, 0].copy()
            alphajold = alpha[j, 0].copy()
            if (Y[i, 0] != Y[j, 0]):
                L = max(0, alpha[j, 0] - alpha[i, 0])
                H = min(C, C+alpha[j, 0] - alpha[i, 0])
            else:
                L = max(0, alpha[j, 0] + alpha[i, 0] - C)
                H = min(C, alpha[j, 0] + alpha[i, 0])
            eta = 2.0* X[i, :] * X[j, :].T - X[i, :] * X[i, :].T -X[j, :] * X[j, :].T
            alpha[j] -= Y[j, 0] * (ei - ej)/eta
            alpha[j] = clipalpha(alpha[j], H, L)

            alpha[i] += Y[j, 0] * Y[i, 0] * (alphajold - alpha[j, 0])   # 最关键的是更新两个alpha
            b1 = b - ei - Y[i,0]*(alpha[i,0]-alphaiold) * X[i,:] * X[i, :].T - Y[j,0]*(alpha[j,0]-alphajold) * X[j,:] * X[j, :].T
            b2 = b - ej - Y[i,0]*(alpha[i,0]-alphaiold) * X[i,:] * X[i, :].T - Y[j,0]*(alpha[j,0]-alphajold) * X[j,:] * X[j, :].T
            if  (0<alpha[i, 0]) and (C>alpha[i,0]):
                b = b1
            elif (0<alpha[j, 0]) and (C>alpha[j,0]):
                b = b2
            else:
                b = b1 + b2
        iter += 1
for i in range(m):
    if alpha[i, 0] < 0.01:
        alpha[i, 0] = 0

w = np.multiply(alpha, Y).T * X

tt=0
maxalpha = 0
for i in range(m):
    if alpha[i, 0]> maxalpha:
        maxalpha = alpha[i,0]
        tt = i
b = Y[tt,0] -  np.dot(w,X[tt].T)

x231 = np.linspace(0,10,200)
y231 = -(w[0,0] * x231 + float(b))/w[0,1]
plt.plot(x231,y231)
plt.show()












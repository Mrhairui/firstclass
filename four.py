import numpy as np
x1 = []
x2 = []
y = []
for i in range(-10, 10):
    x1.append(i)
    j = np.random.randint(-10, 10)
    x2.append(j)
    t = i + 2 * j - 3
    if t > 0:
        y.append(1)
    else:
        y.append(0)


X = [x1, x2]
w = np.mat([0, 0])
X = np.mat(X).T
y = np.mat(y).T
alpha = 0.01
errormin = np.inf
for k in range(1000):
    f = w * X.T
    f1 = 1 / (1 + np.exp(-f))
    error = f1.T - y
    w = w.T - alpha * X.T * error
    w = w.T
    error1 = np.sum(np.array(error)[:, 0]**2)
    if error1 < errormin:
        errormin = error1
        print(errormin / sum(y))

print(errormin/sum(y))









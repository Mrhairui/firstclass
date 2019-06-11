import numpy as np


def load_data():
    fr = open('testSet_1.txt')
    X = []
    for line in fr.readlines():
        line = line.strip().split('\t')
        line1 = [float(data) for data in line]
        X.append(line1)
    return X


def kmeans(X, k):
    X = np.array(X)
    m, n = np.shape(X)
    cent = []
    itermax = 4
    iter = 0
    t = np.zeros((1, k))[0]
    for i in range(k):
        p = int(np.ceil((i / k) * m))
        cent.append(X[p])
    while(iter < itermax):
        rec = []
        iter = iter + 1

        for i in range(m):
            mindis = np.inf
            minrec = np.array([1, 1])
            for center in cent:
                dist = float(np.sqrt(sum(np.power(X[i] - center, 2))))
                if dist < mindis:
                    mindis = dist
                    minrec = center
            rec.append(minrec)
        t = np.zeros((1, k))[0]
        cent1 = cent.copy()
        for tt in range(k):
            cent[tt] = np.array([0.0, 0.0])
        for i in range(m):
            for j in range(k):
                if (rec[i] == cent1[j]).all():
                    cent[j] += X[i]
                    t[j] = t[j] + 1
        for j in range(k):
            cent[j] = cent[j] / t[j]

    return cent, t

X = load_data()
k = 4
cent, t = kmeans(X, k)


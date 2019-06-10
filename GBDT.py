import numpy as np
X = np.arange(1, 11)
Y = np.array([5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05])
s = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]


def cal_error(X, Y, sl):
    numl = 0
    numg = 0
    cl = 0
    cg = 0
    error = 0
    yy = []
    for i in range(10):
        if X[i] <= sl:
            numl = numl + 1
            cl = Y[i] + cl
        else:
            numg = numg + 1
            cg = Y[i] + cg
    cl = cl / numl
    cg = cg / numg
    for i in range(10):
        if X[i] <= sl:
            error = np.square(Y[i] - cl) + error
            yy.append(Y[i] - cl)
        else:
            error = np.square(Y[i] - cg) + error
            yy.append(Y[i] - cg)

    return cl, cg, error, yy


def gbdt(X,Y):
    errormin = np.inf
    cll = []
    cgg = []
    ss = []
    cllmin = 0
    cggmin = 0
    ssmin = 0
    y_min = []
    while(errormin > 0.2):
        for sl in s:
            cl, cg, error, yy = cal_error(X, Y, sl)
            if error < errormin:
                errormin = error
                cllmin = cl
                cggmin = cg
                ssmin = sl
                y_min = yy
        cll.append(cllmin)
        cgg.append(cggmin)
        ss.append(ssmin)
        Y = y_min


    return cll, cgg, ss, errormin


cll, cgg, ss, errormin = gbdt(X,Y)





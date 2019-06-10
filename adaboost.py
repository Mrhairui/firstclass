import numpy as np
x = np.arange(0,10)
y = np.array([1, 1, 1, -1, -1, -1, 1, 1, 1, -1])
threp = [i-0.5 for i in x]
threp.append(9.5)


def cal_thre(x, y, w):
    minerror = np.inf
    threshold = 0
    iit = 'gt'
    yymin = []
    for thre in threp:
        for it in ['gt', 'lt']:
            error = np.zeros((10, 1))
            error_min = 0
            yy = []
            if it == 'gt':
                for i in range(10):
                    if x[i] > thre:
                        yy.append(1)
                    else:
                        yy.append(-1)
                    if yy[i] == y[i]:
                        error[i] = 0
                    else:
                        error[i] = 1
            else:
                for i in range(10):
                    if x[i] > thre:
                        yy.append(-1)
                    else:
                        yy.append(1)
                    if yy[i] == y[i]:
                        error[i] = 0
                    else:
                        error[i] = 1
            error_min = float(np.dot(w.T , error))
            if error_min < minerror:
                minerror = error_min
                threshold = thre
                yymin = yy
                iit = it
    return threshold, iit, minerror, yymin


def adaboost(x, y):
    w = 0.1 * (np.ones((10, 1)))
    alphas = []
    errorpp = np.inf
    errordat = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    for i in range(100):
        threshold, iit, error, yy = cal_thre(x, y, w)
        alpha = 1 / 2 * np.log((1 - error) / error)
        alphas.append(alpha)
        w = np.multiply(np.exp(-alpha * np.multiply(y ,yy)), w.T)
        zz = sum(w[0])
        w = w / zz
        w = w.T
        errordat += np.array([alpha * ypp for ypp in yy])
        errorpp = np.array(errordat) - y
        errorpp1 = sum(errorpp)
        if abs(errorpp1) < 0.01:
            break

    return errorpp1, alphas






error, alphas = adaboost(x,y)






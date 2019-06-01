import numpy as np
import matplotlib.pyplot as plt
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
x11 = []
x12 = []
x21 = []
x22 = []
for i in range(20):
    if y[i] == 1:
        x11.append(x1[i])
        x12.append(x2[i])
    else:
        x21.append(x1[i])
        x22.append(x2[i])
plt.scatter(x11, x12, color='red', s=50)
plt.scatter(x21, x22, color='blue', s=50)
xp = [4, 4]
dismin = np.inf
k = 3
dis = []
for i in range(20):
    dis.append(np.square(x1[i] - xp[0]) + np.square(x2[i] - xp[1]))
for i in range(1, 20):
    t = i
    for j in range(i):
        if dis[t] < dis[t-1]:
            ex = dis[t-1]
            dis[t-1] = dis[t]
            dis[t] = ex
            ey = y[t-1]
            y[t-1] = y[t]
            y[t] = ey
            t = t - 1
        else:
            break
b = 0
c = 0
for i in range(k):
    if y[i] == 1:
        b = b+1
    else:
        c = c + 1

if b > c:
    yy = 1
    plt.scatter(xp[0], xp[1],color='red', s=200)
else:
    plt.scatter(xp[0], xp[1], color='blue', s=200)

plt.show()













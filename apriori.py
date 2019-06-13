

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataset):
    c1 = []
    itemn = {}
    length = len(dataset)
    tt = 0
    for transaction in dataset:
        for item in transaction:
            if item not in c1:
                c1.append(item)
    c1 = [frozenset([item]) for item in c1]
    return c1


def scan(dataset, Ck, minsupport):
    ss = {}
    length = len(dataset)
    for transaction in dataset:
        for ck in Ck:
            if ck.issubset(transaction):
                if ck not in ss.keys():
                    ss[ck] = 1
                else:
                    ss[ck] += 1
    retlist = []
    supportdata = {}
    for key in ss.keys():
        if ss[key] / length < minsupport:
            retlist.append(key)
        supportdata[key] = ss[key] / length
    return retlist, supportdata


def apriorigen(Lk, k):  # 两个集合求合并
    lenlk = len(Lk)
    retlist = []
    for i in range(lenlk):
        for j in range(i, lenlk):
            L1 = list(Lk[i])[:, k-2]
            L2 = list(Lk[i])[:, k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retlist.append(Lk[i] | Lk[j])
            return retlist

def apriori(dataset, minsupport):
    c1 = createC1(dataset)
    L1, supportdata = scan(dataset, c1, minsupport)
    k = 2
    L = [L1]
    while(len(L[k-2]) > 0):
        Ck = apriorigen(L[k-2], k)
        Lk, supk = scan(dataset, Ck, minsupport)
        supportdata.updata(supk)   # updata 相当于列表里面的append
        L.append(Lk)
        k+=1
        return L, supportdata


dataset = loadDataSet()
L,supportdata = apriori(dataset, 0.7)






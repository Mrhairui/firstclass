class treenode:
    def __init__(self, namevalue, numoccur, parentnode):
        self.name = namevalue
        self.count = numoccur
        self.nodelink = None
        self.parent = parentnode
        self.children = {}

    def inc(self, numoccur):
        self.count += numoccur

    def disp(self, ind = 1):
        print(' '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)


def loaddata():
    dataset = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return dataset


def createtree(dataset, minsup=1):
    headertable = {}
    for trans in dataset:
        for item in trans:
            headertable[item] = headertable.get(item, 0) + 1   # get返回制定key的值, 如果key不存在则返回0
    for k in list(headertable.keys()):                         # 如何删除字典中的元素
        if headertable[k] < minsup:
            del(headertable[k])
    freqitem = set(headertable.keys())
    for k in headertable.keys():
        headertable[k] = [headertable[k], None]
    rettree = treenode('Null set', 1, None)
    for transet in dataset:
        localD = {}
        for item in transet:
            if item in freqitem:
                localD[item] = headertable[item][0]
        if len(localD) > 0:
            ordereditem = [v[0] for v in sorted(localD.items(), key = lambda p:p[1], reverse = True)]  # 字典的排序
            updatetree(ordereditem, rettree, headertable, 1)
    return rettree, headertable


def updatetree(ordereditem, rettree, headertable, count):
    if ordereditem[0] in rettree.children:
        rettree.children[ordereditem[0]].inc(count)
    else:
        rettree.children[ordereditem[0]] = treenode(ordereditem[0], count, rettree)

        if headertable[ordereditem[0]][1] == None:
            headertable[ordereditem[0]][1] = rettree.children[ordereditem[0]]
        else:
            updateheader(headertable[ordereditem[0]][1], rettree.children[ordereditem[0]])

    if len(ordereditem) > 1:
        updatetree(ordereditem[1:], rettree.children[ordereditem[0]], headertable, count)


def updateheader(nodetotest, targetnode):
    while(nodetotest.nodelink != None):
        nodetotest = nodetotest.nodelink
    nodetotest.nodelink = targetnode


dataset = loaddata()
tree, headertable = createtree(dataset, 3)








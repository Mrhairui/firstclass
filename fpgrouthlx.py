class treenode:
    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.nodelink = None
        self.children = {}
        self.parent = parent

    def inc(self, count):
        self.count += count

    def disp(self, ind=1):
        print(' '*ind, self.name, ' '*ind, self.count)
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


dataset = loaddata()


def createtree(dataset, minsup):

    headertable = {}
    for trans in dataset:
        for item in trans:
            if item not in headertable.keys():
                headertable[item] = 1
            else:
                headertable[item] += 1

    for k in list(headertable.keys()):
        if headertable[k] < minsup:
            del(headertable[k])
    freqitem = set(headertable.keys())
    for k in headertable.keys():
        headertable[k] = [headertable[k], None]
    tree = treenode('Null', 1, None)
    for tran in dataset:
        data = {}
        for item in tran:
            if item in freqitem:
                data[item] = headertable[item][0]
        if len(data) > 0:
            data = [v[0] for v in sorted(data.items(), key = lambda p: p[1], reverse = True)]
            if data[0] in tree.children:
                tree.children[data[0]].inc(1)
            else:
                tree.children[data[0]] = treenode(data[0], 1, tree)
            if headertable[data[0]][1] == None:
                headertable[data[0]][1] = tree.children[data[0]]
            else:
                while ()

            b = tree.children[data[0]]
            if len(data) > 1:
                for i in range(1, len(data)):
                    if data[i] in b.children:
                        b.children[data[i]].inc(1)
                    else:
                        b.children[data[i]] = treenode(data[i], 1, b)
                    b = b.children[data[i]]












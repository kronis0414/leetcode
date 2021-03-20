class NestedIterator:
    def __init__(self, nestedList):
        self.tmp = []
        self.idx = 0
        def flatten(nL):

            for e in nL:
                if e.isInteger():
                    self.tmp.append(e.getInteger())
                else:
                    flatten(e.getList())
        flatten(nestedList)
        
    def next(self):
        v = self.tmp[self.idx]
        self.idx += 1
        return v
    
    def hasNext(self):
        if self.idx == len(self.tmp):
            return False
        return True
#只要在初始時, 遞迴地展開nestedList, 並放入暫存中
#再以一個point指向目前的元素位置
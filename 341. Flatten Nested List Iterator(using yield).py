class NestedIterator:
    def __init__(self, nestedList):
        def geneNext(nL = nestedList):
            for e in nL:
                if e.isInteger():
                    yield e.getInteger()
                else:
                    yield from geneNext(e.getList())
        self.g = geneNext()
        
    def next(self):
        return self.v
    
    def hasNext(self):
        try:
            self.v = next(self.g)
            return True
        except:
            return False
            
#可以用coroutine來實現, 如果元素是integer就直接yield
#否則就得用yield from遞迴呼叫
#當在hasNext時, 試著存取下一個值, 如果有下一個值, 則先保存起來, 等待next被呼叫時可以回傳
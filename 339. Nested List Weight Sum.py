class Solution:
    def depthSum(self, nestedList):
        self.s = 0
        self.run(nestedList, 1)
        return self.s
    def run(self, nestedList, deep):
        
        for n in nestedList:
            if n.isInteger():
                self.s += (n.getInteger() * deep)
            else:
                self.run(n.getList(), deep + 1)
#若n為list則不斷地遞迴, 每次深度加1, 
#否則將n乘以深度加總
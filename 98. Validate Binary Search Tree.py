class Solution:
    def isValidBST(self, root):
        if root == None: return True
        self.tmp = []
        self.run(root)
        for i in range(1, len(self.tmp)):
            if self.tmp[i-1] >= self.tmp[i]:
                return False
        return True
    def run(self, root):
        if root == None: return
        self.run(root.left)
        self.tmp.append(root.val)
        self.run(root.right)
#用inorder traversal, 若是真的有效的2元搜尋樹
#即會得到由小到大的traversal結果
#所以藉由這個特性, 只要檢查得到的tmp是否由小到大排列即可
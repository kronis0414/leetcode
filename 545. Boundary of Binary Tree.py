class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        ans = []
        if root.left or root.right:
            ans.append(root.val)
        t = root.left
        while t:
            if t.left or t.right:
                ans.append(t.val)
            if t.left:
                t = t.left
            else:
                t = t.right
        self.addLeaves(root, ans)
        t = root.right
        stk = []
        while t:
            if t.left or t.right:
                stk.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        while stk:
            ans.append(stk.pop())
        return ans
    def addLeaves(self, root, ans):
        if not root:
            return
        if root.left == None and root.right == None:
            ans.append(root.val)
            return
        self.addLeaves(root.left, ans)
        self.addLeaves(root.right, ans)
#分成3部分
#1.左邊的node
#2.葉子
#3.右邊的node
#
#1.先沿著左邊的node, 若該點有任何一個child, 表示還沒到leave, 所以push該點的值到ans
#  並以左child為優先, 若該node有左child, 表示該左child為boundary node, 所以
#  往左節點方向去
#2.用preorder的traversal的方式去探索leave的node
#3.跟1.一樣, 只不過換成右node
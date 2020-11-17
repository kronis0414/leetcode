class Solution:
    def flatten(self, root):
        if not root:
            return []
        
        stk = [root]
        
        last = TreeNode(-1)
                
        while stk:
            n = stk.pop()
            last.right = n
            if n.right:
                stk.append(n.right)
            if n.left:
                stk.append(n.left)
            #將原本節點的左子樹清空
            n.left = None
            #將原本節點的右子樹清空
            n.right = None
            #last往下移一個node
            last = n

        return root

#有點像深度優先探索(DFS)
#1.使用last來標示處理完後最後的葉子
#2.因為left節點必須比right優先被處理, 所以在push節點進stk時, 先push右節點, 再push左節點, 因為stack的特性
#3.先把左子樹處理完, 再pop右子樹的節點繼續處理, pop之後順便把它接在last的最右邊

class Solution:
    def verticalTraversal(self, root):
        memo = {}
        
        def r(n, vertical, level):
            if n:
                if vertical not in memo:
                    memo[vertical] = [[level, n.val]]
                else:
                    memo[vertical].append([level, n.val])
                r(n.left, vertical - 1, level + 1)
                r(n.right, vertical + 1, level + 1)
        r(root, 0, 0)

        return [[v[1] for v in sorted(memo[k])] for k in sorted(memo)]
        
#水平方向, root為0, 向左減1, 向右加1, 以此類推
#垂直方向, root為第0層, 子樹就增加1層, 以此類推
#因為要求的答案是從左邊看過來的二元數, 以及從上到下
#所以先以水平排序, 在分別對每個水平方向的元素, 從上到下排序
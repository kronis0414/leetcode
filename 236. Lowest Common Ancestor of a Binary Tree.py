class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {}
        
        stk = [root]
        while stk:
            n = stk.pop()
            if n.left:
                parent[n.left] = n
                stk.append(n.left)
            if n.right:
                parent[n.right] = n
                stk.append(n.right)
        p_parent = set([p])
        
        while p in parent:
            p_parent.add(parent[p])
            p = parent[p]
            
        while q not in p_parent:
            q = parent[q]
        
        return q
        
#先建立每個node的parent是誰
#然後把p或q的parent全部先找出來(比如找p的parent)
#然後再找q的parent, 當q遇到的parent出現在p的parent清單裡, 則它就是LCA
#否則不斷的找q的parent
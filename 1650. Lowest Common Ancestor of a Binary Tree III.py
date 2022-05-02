class Solution:
    def lowestCommonAncestor(self, p, q):
        rec = dict()
        while p != None:
            rec[p.val] = p
            p = p.parent
        while q != None:
            if q.val in rec:
                return rec[q.val]
            q = q.parent
            
# 題目只給2個node, 且node有pointer指向自己的parent
# 所以只要把其中一個node的所有parent記錄下來
# 另一個node, 再去看他的parent, 若遇到有重複的parent
# 則這個重複的parent即是lowest common ancestor
class Solution:
    def rob(self, root):

        def run(n):
            if n == None:
                return 0, 0
            #include, not include
            if n.left == None and n.right == None:
                return n.val, 0
            v = n.val
            leftV_include, leftV_notInclude = run(n.left)
            rightV_include, rightV_notInclude = run(n.right)

            return v + leftV_notInclude + rightV_notInclude, leftV_include + rightV_include
        v1, v2 = run(root)
        return max(v1, v2)

#dfs, 不斷的從根往下到葉子, 然後往上回傳子節點的值
#每個節點一次要回傳2種值
#1種是從葉子到包含該節點(自己)的加總值
#另1種則是從葉子到不包含該節點的加總值
#往上回傳時, 為了回傳包含目前節點的值, 所以就是目前節點的值去加上不包含左右子節點的值
#為了回傳不包含目前節點的值, 所以無論是否包含子節點的值都能往上回傳, 所以就找最大左右子節點相加往上回傳
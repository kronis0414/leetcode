class Solution:
    def numTrees(self, n):
        memo = []
        memo.append(1)
        memo.append(1)
        l = 0
        r = n - 1
        for i in range(2, n + 1):
            l = 0
            r = i - 1
            tmp = 0
            while r >= 0:
                tmp += memo[l] * memo[r]
                r -= 1
                l += 1
            memo.append(tmp)
        return memo[n]
        
#分別記錄左子樹和右子樹所能產生的二元數數量
#root固定一個node, 則左子樹有0~n-1個子樹數量, 右子數有n-1~0個子樹數量, 
#也就是當左子樹0個node時, 右子樹有n-1(因為root佔了一個)個node
#每次將左子樹數量和右子樹數量相乘相加(從0~n-1), 即是當前n所能產生的2元搜尋樹數量
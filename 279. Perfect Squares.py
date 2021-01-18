class Solution:
    def numSquares(self, n):
        coins = [v ** 2 for v in range(1, int(n ** 0.5) + 1)]
        memo = [float('inf')] * (n+1)
        memo[0] = 0
        
        for c in coins:
            for i in range(c, n + 1):
                memo[i] = min(memo[i], memo[i-c] + 1)
        return memo[-1]
#該問題能夠轉換成最少硬幣個數問題
#也就是給一個數字, 以及擁有的硬幣種類, 1元, 5元...等等
#這裡的硬幣種類即是square number, 1, 4, 9, 16, 25...
#然後在執行最少硬幣個數算法
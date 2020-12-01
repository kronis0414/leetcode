class Solution:
    def coinChange(self, coins, amount):
        memo = [float('INF')] * (amount+1)
        
        memo[0] = 0
        
        for c in coins:
            for a in range(c, amount+1):
                memo[a] = min(memo[a], memo[a-c] + 1)
                
        return memo[-1] if memo[amount] != float('INF') else -1
        
#322求的是最少硬幣組合數量
#518求的是有多少組硬幣

#用一個array紀錄由總數1到amount, memo[i]表示金錢數i時的最少硬幣個數
#因為是計算最少個數, 所以初始時都無限大, 金錢數量0時, 需要的硬幣數也為0
#若要計算memo[i], 則需要考慮當前memo[i]數量, 以及memo[i-c], c為某個硬幣值
#代表使用當前硬幣c, 金錢數減去c的個數memo[i-c], 2者相加是否小於當前memo[i],

#example:
#coins = [c1, c2, c3]
#F(3) = min(F(3-c1), F(3-c2), F(3-c3)) + 1


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
#322求的是最少硬幣組合數量
#518求的是有多少組硬幣

#求的是組合數量, 所以初始均為0, 組合金錢0, 所需要的硬幣為0個, 也算1組
#使用一個dp陣列儲存組合數量, dp[i]代表在組合金錢i時, 所能形成的組合數量
#因為算的是組合, 計算dp[i]時, 且硬幣為c, 只要把dp[i-c]的數量加起來就可以

#example
#coins = [1, 2, 5]
#F(5) = F(5-1) + F(5-2) + F(5-5)

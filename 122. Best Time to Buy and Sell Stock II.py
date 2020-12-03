class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        n = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if n < prices[i]:
                profit += prices[i] - n
            n = prices[i]
        return profit
#跟121類似
#122可以多買多賣
#因為可以多次買賣, 所以最大的利益一定是遇到低買, 遇到高就賣, 一直不斷重複
#假設若有1到n個數值
#A, B是數值之間低買高賣的profit, Z是1-n之間最小stock的減去最大的stock
#則A+B 一定大於等於Z

#11
#10
#9                     *(p2)
#8
#7              
#6              
#5        *(p1)
#4              *(v2)
#3       
#2     *(v1)
#1

#若A = p1-v1, B = p2-v2, Z=p2-v1
#最大利益一定是A+B, 不會是Z
#若假設v2 >= p1, 則A+B一定等於Z
class Solution:
    def maxProfit(self, prices):
        profit = 0
        left_min = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > left_min:
                profit = max(profit, prices[i]-left_min)
            else:
                left_min = prices[i]
        return profit
        
class Solution:
    def maxProfit(self, prices):
        
        if len(prices) <= 1:
            return 0
        profit = 0
        left_min = prices[0]
        for i in range(1, len(prices)):
            #計算當下profit值
            if prices[i] - left_min > profit:
                profit = prices[i] - left_min
            #更新左邊最小
            if prices[i] < left_min:
                left_min = prices[i]
        return profit
        
#保存左邊的最小值, 然後更新他, 每次遇到一個新值, 計算當下利益多少
#上面都是相同概念
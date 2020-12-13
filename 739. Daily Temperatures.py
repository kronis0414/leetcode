class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stk = []
        for i in range(len(T)-1, -1, -1):
            while stk and T[stk[-1]] <= T[i]:
                stk.pop()
            if stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans
#從list的右邊向左iteration
#stk裡面放的是溫度從大到小所對應的索引
#當目前的溫度T[i]比stk的頂端溫度還要高時, 表示目前stk的頂端不是答案
#需要pop stk直到stk頂端溫度大於目前的溫度
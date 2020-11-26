class Solution:
    def trap(self, height):
        ans = 0
        stk = []
        for i in range(len(height)):
            while stk and height[stk[-1]] < height[i]:
                idx = stk.pop()
                if stk:
                    ans += (min(height[stk[-1]], height[i]) - height[idx]) \
                        * (i - stk[-1] - 1)
            stk.append(i)
        return ans

#使用stk作為暫存, 放的是索引值
#stk裡面的內容是由大到小的非遞增排列的bar,
#若stk放的是由小到大的非遞減bar則就沒有計算的意義, 因為height是從左掃到右, 若是一直非遞減則無法蓄水
#所以要放成非遞增
#有兩種情況
#1.若當stk的top比現在的bar來的還要大或相同, 則把現在的bar放入stk中, 使stk裡的bar呈現非遞增的狀態
#2.若stk的top比現在的bar來的要小, 要計算的蓄水量範圍是現在的bar和stk之間, 
#  不直接跟stk的top運算, 是因為它沒有形成一個凹槽, 
#  所以需要把stk的最後一個元素pop掉, 當作凹槽來儲水, 
#  要計算的蓄水高度為
#  現在bar的高度以及stk的top高度的最小值減去凹槽的高度
#  要計算的蓄水寬度為
#  現在bar的索引值減去stk的top的索引值
#另外現在的bar和stk的top之間, 不會出現高度大於現有的bar和stk的top, 因為已經被處理完了, 該bar會放在stk內
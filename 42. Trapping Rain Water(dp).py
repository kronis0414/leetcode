class Solution:
    def trap(self, height):
        n = len(height)
        if not n:
            return 0
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        ans = 0
        
        for i in range(1, n-1):
            ans += min(left_max[i], right_max[i]) - height[i]
        
        return ans

#因為積水是左右2邊的高度大於自己所形成的區域
#所以用2個array暫存, 從左邊(left_max)或從右邊(right_max)看過來的最大值, 
#在每次循環時只要查看左邊右邊的最小高度, 在減去當前高度, 即是積水區域
#其中, 在計算left_max[i]或right_max[i]時, 也考慮height[i], 目的是為了減少一次if判斷
#假設left_max[i], right_max[i]不包含height[i], 若height[i]是所有height裡面最高的
#則左邊右邊的最小高度減去height[i], 會得到負數, 得需要加if判斷去處理
#包含自己的話, 左邊右邊的最小高度減去height[i]會得到0, 不影響結果



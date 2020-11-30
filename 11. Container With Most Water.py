class Solution:
    def maxArea(self, height):
        ans = 0
        
        left = 0
        right = len(height) - 1
        
        while right > left:
            dist = right - left
            area = dist * min(height[left], height[right])
            if area > ans:
                ans = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans
#使用2個指標分別在左和右, 過程中不斷計算當前面積並更新答案
#移動最小高度的指標理由是, 因為在此時此刻, 該最小指標已經達到它的最大值, 以下為證明
#
#假設移動高度高的指標, 設height[left] < height[right], 所以移動right指標
#在left到right(不包含right)的之間的某個指標p, 
#1. 若height[left] > height[p]
#   因為計算是採最小高度, 所以高度會是height[p], 而且距離會比left到right來的小
#   所以不會是答案
#2. 若height[left] < height[p]
#   因為計算是採最小高度, 所以高度會是height[left], 而且距離會比left到right來的小
#   也就是height[left]在height[right]時, 就已經是最佳答案
#根據上述, 所以要移動高度小的指標
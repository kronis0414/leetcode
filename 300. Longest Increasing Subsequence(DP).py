class Solution:
    def lengthOfLIS(self, nums):
        memo = [0] * len(nums)
        ans = 0
        for i in range(len(nums)):
            curMaxlength = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curMaxlength = max(curMaxlength, memo[j])
            memo[i] = curMaxlength + 1
            ans = max(ans, memo[i])
        return ans
#宣告一個memo[i], 表示在nums[i]時最大的遞增序列
#所以要計算nums[i]時, 就去找最大的nums[j], 0<= j < i, 然後加1, 在每次計算memo[i]時, 就更新ans
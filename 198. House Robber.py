class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        k2 = 0
        k1 = nums[0]
        
        for i in range(1, len(nums)):
            k = max(k2 + nums[i], k1)
            k2, k1 = k1, k
            
        return k1

#使用dp解決, 計算
#令f(k)為從第0個house到第k個house最大的數量
#所以f(K)=max(f(k-1), f(k-2) + nums[k])
#分別表示在k個house時, 不偷或偷第k個house

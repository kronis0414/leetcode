class Solution:
    def maxSubArray(self, nums):
        ans = float('-inf')
        tmp = 0
        for n in nums:
            if tmp < 0:
                tmp = n
            else:
                tmp += n
            if tmp > ans:
                ans = tmp
        return ans
#用一個變數tmp累積前面所計算的結果
#若tmp是負數則不用考慮其他情況, 直接把tmp設成n
#因為1.若n是正數, 則tmp + n不會大於n, 
#    2.若n是負數, 則tmp + n越加越小


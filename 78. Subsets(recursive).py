class Solution:
    def subsets(self, nums):
        ans = []
        
        def run(si, tmp):
            ans.append(tmp.copy())
            for i in range(si, len(nums)):
                tmp.append(nums[i])
                run(i + 1, tmp)
                tmp.pop()
                
        run(0, [])
        return ans
#用遞迴的很簡單就能得出所有的子集合
#每次迴圈的起始索引是上次被處理元素的下一個
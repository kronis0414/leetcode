class Solution:
    def findDuplicates(self, nums):
        ans = []
        
        for i, n in enumerate(nums):
            while nums[i] != i + 1 and nums[i] != -1:
                corp_idx = nums[i] - 1
                if nums[corp_idx] == -1:
                    nums[corp_idx] = nums[i]
                    nums[i] = -1
                    break
                if nums[i] == nums[corp_idx] :
                    ans.append(nums[i])
                    nums[i] = -1
                    break
                nums[i], nums[corp_idx] = nums[corp_idx], nums[i]
                
        return ans
#因為題目要求不能使用額外的空間, 所以只能用原本的nums來改
#想出來的方法速度慢, 網路上有更好解法
#思路是
#若原本索引i+1和他對應的元素值nums[i]不相等, 就一直交換, 換到i+1 == nums[i]才結束
#換的途中若遇到要放的位置裡面元素內容和自己相同, 也就是遇到重複元素nums[i] == nums[corp_idx], 
#所以把他push到答案, 並且把重複的元素的索引內容設成-1, 結束while迴圈
#換的途中若遇到要放的位置裡面元素為-1, 那就直接把值給放進去, 並結束while迴圈
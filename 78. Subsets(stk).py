class Solution:
    def subsets(self, nums):
        ans = [[]]
        stk = [[[None], -1]]
        while len(stk) is not 0:
            subset, i = stk.pop()
            if i < len(nums):
                subset.pop()
                while i < len(nums)-1:
                    subset.append(nums[i+1])
                    stk.append([subset.copy(), i + 1])
                    ans.append(subset.copy())
                    i += 1
        return ans
#使用一個stk, 當作候選, 裡面元素是一個list
#list放的是已經被加入到ans裡面的子集合, 和一個起始索引
#起始索引代表該子集合, 下一個需要被加入的元素
#所以從stk挑一個候選出來後, 先把最後一個元素給pop掉, 
#從給定的索引位置加入元素形成新的子集合

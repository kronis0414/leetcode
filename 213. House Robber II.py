class Solution:
    def rob(self, nums):
        pre1 = nums[-1]
        pre2 = nums[-1]
        ans1 = 0
        ans2 = 0
        for i in range(1, len(nums) - 2):
            v = max(nums[i] + pre2, pre1)
            pre2, pre1 = pre1, v
        ans1 = pre1

        pre1 = 0
        pre2 = 0
        for i in range(0, len(nums) - 1):
            v = max(nums[i] + pre2, pre1)
            pre2, pre1 = pre1, v
        ans2 = pre1

        return max(ans1, ans2)

#因為頭尾接在一起, 所以要考慮2種情況
#答案一定是出現在某個元素取或不取的情況下
#用nums最後一個元素作為例子
#假設取最後一個元素, 那麼他旁邊的元素肯定是不能取, 所以就得從第1個判斷到倒數第3個
#-3 -2 -1  0  1  2
#?   x  y  x  ?  ?
#假設不取最後一個元素, 那他旁邊的元素可取或可不取, 所以就得從第0個判斷到倒數第2個
#-3 -2 -1  0  1  2
#?   ?  x  ?  ?  ?
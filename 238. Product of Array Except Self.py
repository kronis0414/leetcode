class Solution:
    def productExceptSelf(self, nums):
        output = nums.copy()
        
        output[-2] = output[-1]
        output[-1] = 1
        for i in range(-3, -len(nums)-1, -1):
            output[i] = output[i+1] * nums[i+1]
            
        for i in range(1, len(nums)):
            output[i] = output[i] * nums[i-1]
            nums[i] = nums[i] * nums[i-1]
            
        return output
#將output拿來當作暫存
#第一個迴圈是把陣列從右成到左, 放入output內,
#也就是output[i]等於nums[i+1] * nums[i+2] * ...到array底的乘積
#在第二個迴圈計算題目要的答案時, 再把左邊的乘積放入nums內
#也就是nums[i] = nums[i] * nums[i-1] *...* nums[0]
#計算答案output[i], 因為output[i]本身不包含原始的nums[i], 且nums[i-1]是左邊的乘積
#所以直接把output[i]和nums[i-1]相乘, 即是output[i]的答案
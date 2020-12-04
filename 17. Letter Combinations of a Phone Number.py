class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        memo = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno'
                , '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        ans = []
        def r(idx, s):
            if len(digits) == idx:
                ans.append(s)
                return
            
            for i in range(len(memo[digits[idx]])):
                r(idx + 1, s + memo[digits[idx]][i])
        r(0, '')
        return ans
#使用recursive
#建一個數字和字母對應關係memo
#
#從digits第0個數字字元開始, 循環該數字字元所對應字母字串, 取得該字串的某個字母後
#再遞迴的呼叫下一個數字字元, 若idx等於字串長度, 代表已經完成一個字串的拼接, 放入答案裡
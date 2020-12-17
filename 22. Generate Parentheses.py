class Solution:
    def generateParenthesis(self, n):
        self.ans = []
        self.run(0, 0, n, '')
        return self.ans
    def run(self, l, r, n, tmp):
        if r == n:
            self.ans.append(tmp)
            return
        
        if l < n:
            self.run(l+1, r, n, tmp + '(')
        
        if l > r:
            self.run(l, r+1, n, tmp + ')')
#遞迴的生成
#先從左括號開始, 一直增加左號, 然後再增加右括號
#增加右括號過程中, 須注意不能超過左括號的數量
class Solution:
    def romanToInt(self, s):
        memo = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        ans = 0
        pre = ''
        for c in s:
            if pre == 'I' and (c == 'V' or c == 'X'):
                ans += memo[c] - memo[pre] * 2
            elif pre == 'X' and (c == 'L' or c == 'C'):
                ans += memo[c] - memo[pre] * 2
            elif pre == 'C' and (c == 'D' or c == 'M'):
                ans += memo[c] - memo[pre] * 2
            else:
                ans += memo[c]
            pre = c
        return ans
#先把字母的值用字典保存
#然後保存前一個羅馬字母, 若遇到是有5開頭的字母則需要特殊處理
#以及要減去之前加的字母, 所以* 2
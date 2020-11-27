class Solution:
    def numDecodings(self, s):
        if s[0] == '0':
            return 0
        p_1 = 1
        p_2 = 1
        
        for i in range(1, len(s)):
            v = 0
            c1 = int(s[i])
            if c1 >= 1 and c1 <= 9:
                v += p_1
            c2 = int(s[i-1: i+1])
            if c2 >= 10 and c2 <= 26:
                v += p_2
                
            p_2 = p_1
            p_1 = v
                
        return p_1
        
#使用dynamic programming
#原本使用一個陣列tmp, 紀錄字串從索引0到i時所能解碼的個數
#但後來發現當計算tmp[i]時只需用到tmp[i-1]和tmp[i-2], 所以用p_1和p_2取代
#初始時p_1代表s[0]的解碼個數, 也就是1
#p_2代表空字串解碼個數, 也就是1
#當要計算s[:i+1]解碼個數時, 需要考慮2種情況
#1. s[i], 也就是只有一個字元時, 若s[i]合法, 則解碼次數等於索引0到i-1字串解碼個數, 即p_1
#2. s[i-1, i+1], 有二個字元時, 若s[i-1,i+1]合法, 則解碼個數等於索引0到i-2字串解碼次數, 即p_2
#將2次判斷結果加起來, 即是當前的解碼個數, 將p_1和p_2往前移
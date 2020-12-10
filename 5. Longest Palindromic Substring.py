class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            tmp = ''
            tmp = self.run(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            tmp = self.run(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    def run(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
#從左到右一個一個字元檢視他是否是迴文, 分成以自己為中心向2側擴展, 和2個相同字元向2側擴展
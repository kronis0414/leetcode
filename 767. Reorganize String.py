class Solution:
    def reorganizeString(self, S):
        memo = collections.defaultdict(int)
        
        for c in S:
            memo[c] += 1

        memo = sorted(memo.items(), key=lambda x:x[1], reverse=True)
        memo = [list(item) for item in memo]
        s = sum([memo[i][1] for i in range(1, len(memo))])
        if memo[0][1] > s + 1:
            return ''
        ans = [''] * len(memo) * memo[0][1]
        i = 0
        j = 1
        k = 0
        while i < len(memo):
            while memo[i][1] > 0:
                ans[k] = memo[i][0]
                memo[i][1] -= 1
                k += len(memo)
                if k >= len(ans):
                    k = j
                    j += 1
            else:
                i += 1
        return ''.join(ans)
        
#先計數每個字元的出現次數, 根據出現次數由大到小排序
#若最大的出現次數大於剩餘其他所有的次數加總+1, 則表示無法形成字串
#然後穿插插入字母, 比如aaabbbbc
#a a a
#ab ab ab
#abc ab ab
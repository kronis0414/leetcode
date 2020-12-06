class Solution:
    def partitionLabels(self, S):
        memo = [-1] * 26
        for i, c in enumerate(S):
            memo[ord(c)-ord('a')] = i
        
        i = 0
        ans = []
        while i < len(S):
            bound = memo[ord(S[i]) - ord('a')]
            j = i
            while j <= bound:
                if memo[ord(S[j]) - ord('a')] > bound:
                    bound = memo[ord(S[j]) - ord('a')]
                j += 1
            ans.append(j-i)
            i = j
        return ans
#使用memo紀錄每一個字母最後出現的索引
#從S字串, 往左到右, 從當前字元開始, 該字元的所對應到的最後索引為bound, 
#一直不斷的往bound前進, 每遇到一個字元就更新邊界bound, 若該字元最後出現的索引大於bound, 則更新bound
#若到達邊界, 則代表已經到達字串需要分割的位置, 計算起始字元和bound的差, 得到分割字串長度
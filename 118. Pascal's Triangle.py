class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        ans = [[1]]
        
        for i in range(2, numRows + 1):
            tmp = [1]
            #因為i-1層比i層少一個元素, 所以要減1
            for j in range(1, i - 1):
                tmp.append(ans[-1][j-1] + ans[-1][j])
            tmp.append(1)
            ans.append(tmp.copy())
        return ans
#層的編號從1開始
#i表示目前所要構造的層
#從i-1層構造i層, 所以ans[-1]

class Solution:
    def maximalSquare(self, matrix):
        
        M = len(matrix)
        N = len(matrix[0])
        
        matrix = [[int(v) for v in r] for r in matrix ]
        
        ans = any([matrix[i][0] for i in range(M)]) or any([matrix[0][i] for i in range(N)]) 
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                    ans = max(ans, matrix[i][j])
        return ans * ans
        
#應另外使用一個array來計算正方形邊長比較好
#這裡直接改原始傳進來的陣列
#另matrix[i][j]為正方形邊的長度, 也就是將的長度記錄在此正方形的最右下角
#所以需要考慮3個方向是否都有1, 否則就會缺一角, 無法形成正方形
#因為求的是面積, 所以最後將計算出來邊長相乘
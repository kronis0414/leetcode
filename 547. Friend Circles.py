class Solution:
    def findCircleNum(self, M):
        N = len(M)
        visited = [0] * N
        
        def rec(i):
            for j in range( N):
                if visited[j] == 0 and M[i][j] == 1:
                    visited[j] = 1
                    rec(j)
        
        ans = 0
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                ans += 1
                rec(i)
        return ans
        
#利用遞迴處理, 使用visited作為標記, 代表該編號已經處理過
#1.在第i row時, 若該i尚未處理, 則去循環該row
#2.若M[i][j] = 1, 表示編號i和j有關係, j表示從第0到N-1的column
#3.接著遞迴處理第j row, 不斷重複1-3, 


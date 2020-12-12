class Solution:
    def minPathSum(self, grid):
        tmp = grid[0].copy()
        
        for i in range(1, len(tmp)):
            tmp[i] = tmp[i] + tmp[i-1]
        
        for i in range(1, len(grid)):
            tmp[0] = grid[i][0] + tmp[0]
            for j in range(1, len(grid[0])):
                tmp[j] = grid[i][j] + min(tmp[j], tmp[j-1])
        return tmp[-1]
#一個dp問題
#因為只能從上面或左邊走, 所以只要比較這2個方向大小, 再加上目前的值, 就是到達此grid[i][j]的最小距離
#tmp[j-1]指的是左邊過來的最小值, tmp[j]則是從上面過來的最小值
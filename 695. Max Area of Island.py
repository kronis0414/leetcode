class Solution:
    def maxAreaOfIsland(self, grid):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        m = len(grid)
        n = len(grid[0])

        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    stk = [[x, y]]
                    #避免重複加入
                    grid[x][y] = -1
                    c = 0
                    while stk:
                        x, y = stk.pop()
                        
                        for i in range(4):
                            tx = x + dx[i]
                            ty = y + dy[i]
                            if tx >= 0 and tx < m and ty >= 0 and ty < n and grid[tx][ty] == 1:
                                grid[tx][ty] = -1
                                stk.append([tx, ty])
                        c += 1
                    max_area = max(max_area, c)
        return max_area
#使用dfs方式去進行探索, 並在原grid做標示, 處理元的island設成-1
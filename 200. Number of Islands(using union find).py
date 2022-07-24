class Solution:
    def findParent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.findParent(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1 = self.findParent(n1)
        p2 = self.findParent(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.rank[p1] += 1
                self.parent[p2] = p1
            self.c -= 1
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        self.parent = []
        self.rank = []
        self.c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.parent.append(i*m + j)
                    self.c += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == '0':
                            continue
                        self.union(i*m+j, x*m+y)
        return self.c

# 使用並查集, 將2維陣列展成1維
# 初始時, 
# parent: 若為1, 則parent為自己, 否則為-1, 
# rank: 均為0
# 
# 在union時, 所有得到的結果判斷都要使用parent才合理, 
# 要找到最根源, 而不是使用原本要union的node
# 否則會得到奇怪結果
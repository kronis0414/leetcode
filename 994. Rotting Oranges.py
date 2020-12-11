import queue
class Solution:
    def orangesRotting(self, grid):
        #N * M
        N = len(grid)
        M = len(grid[0])
        
        fresh = {}
        rotten = queue.deque()
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    fresh[(r, c)] = 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        c = 0
        #一定要判斷freah, 防止最後一步會多計算一次,
        #因為在最後時, 若已經沒有任何fresh了, 但rotten一定還有, 還是得把rotten全部跑完才會離開迴圈
        #所以要加判斷fresh
        while rotten and fresh:
            n = len(rotten)
            c += 1
            for _ in range(n):
                orange = rotten.popleft()
                for i in range(4):
                    x = orange[0] + dx[i]
                    y = orange[1] + dy[i]
                    if (x, y) in fresh:
                        fresh.pop((x ,y))
                        rotten.append((x, y))
        return -1 if fresh else c
#使用bfs概念
#宣告2個變數, fresh用來儲存新鮮的orange, rotten用來儲存成熟的orange
#每次從已經成熟的orange開始, 判斷該orange附近有無fresh的orange
#若有就加入rotten候選裡, 直到該次bfs結束, 換下一輪的rotten orange
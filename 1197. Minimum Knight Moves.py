import queue
class Solution:
    def minKnightMoves(self, x, y):
        if x == 0 and y == 0:
            return 0
        dx = [1, -1,  1, -1, 2, -2,  2, -2]
        dy = [2,  2, -2, -2, 1,  1, -1, -1]
        
        x = abs(x)
        y = abs(y)
        
        q = queue.deque()
        q.append([0, 0])
        seen = set([(0,0)])
        k = 1
        while q:
            for i in range(len(q)):
                p1 = q.popleft()
                for j in range(8):
                    p2 = abs(p1[0] + dx[j]), abs(p1[1] + dy[j])
                    #print(p)
                    if p2 == (x, y) or p2 == (y, x):
                        return k
                    if p2 not in seen and (p2[1], p2[0]) not in seen:
                        seen.add(p2)
                        q.append(p2)
            k += 1
#首先, 無法用最小歐肌理得距離的方式抵達(x,y)
#有幾個事實是
#1.無論是到(-x, y)或(x, -y)或(-x, -y)或(x, y)其距離都一樣, 所以只要考慮x, y都為正的時候
#2.到(x, y)跟(y, x), 距離也一樣, 所以只要到達其中一個, 那就是答案
#所以用一個集合去紀錄已經到過哪些點, 到達(x, y)或(y, x)意思一樣, 然後用bfs方式去探索, 就能得到答案
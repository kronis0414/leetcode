import queue
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        d = 1
        q = queue.deque([root])
        ans = []
        while q:
            tmp_v = []
            if d == 1:
                #左邊取答案, 右邊放候選值
                for _ in range(len(q)):
                    
                    n = q.popleft()
                    tmp_v.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            else:    
                #右邊取答案, 左邊放候選值
                for _ in range(len(q)):
                    n = q.pop()
                    tmp_v.append(n.val)
                    if n.right:
                        q.appendleft(n.right)
                    if n.left:
                        q.appendleft(n.left)
            ans.append(tmp_v)
            d = d * -1
        return ans
#stack只有一個進出口, dequeue有2個進出口, 所以使用dequeue, 為了range(len(q)), 才能知道每次level需讀取多少個node
#若目前方向是左到右, 那麼下個方向就是右到左, 所以得按照順序放left, right的候選值, 反之
#用一個變數d來控制讀取答案和放候選值的方向
#d = 1時, 表示目前方向是從左到右讀取答案, 並從left節點到right節點放入候選值
#d = -1時, 表示目前方向是從右到左讀取答案, 並從right節點到left節點放入候選值
import queue
class Solution:
    def distanceK(self, root, target, K):
        if K == 0:
            return [target.val]
        parent = {}
        
        stk = [root]
        #建立每個node的parent
        while stk:
            n = stk.pop()
            if n.left:
                parent[n.left] = n
                stk.append(n.left)
            if n.right:
                parent[n.right] = n
                stk.append(n.right)
        #避免重複加入
        seen = set([target])
        q = queue.deque([target])
        while K > 0:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left and n.left not in seen:
                    seen.add(n.left)
                    q.append(n.left)
                if n.right and n.right not in seen:
                    seen.add(n.right)
                    q.append(n.right)
                if n in parent and parent[n] not in seen:
                    seen.add(parent[n])
                    q.append(parent[n])
            K -= 1
            
        return [v.val for v in list(q)]
        return list(q)
#先建立每個node的parent
#再利用BFS方式去探索
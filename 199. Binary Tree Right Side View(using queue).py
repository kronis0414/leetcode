import queue
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        ans = []
          
        q = queue.deque()
        q.append(root)
        
        while q:
            ans.append(q[-1].val)
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return ans
        
#level order traversal
#一層一層的去展開, 每層的最後一個元素即是從右邊看到的值
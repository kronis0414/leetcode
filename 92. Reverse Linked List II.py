class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        node = ListNode(-1)
        node.next = head
        beginNode = node
        while m > 1:
            beginNode = beginNode.next
            m -= 1
        
        tailNode = head
        while n > 1:
            tailNode = tailNode.next
            n -= 1

        r = tailNode.next
        reverse_head = self.run(beginNode.next, tailNode)
        
        beginNode.next.next = r
        beginNode.next = reverse_head
        return node.next
    def run(self, node, targetNode):
        print(node.val)
        if node == targetNode:
            return targetNode
        n = self.run(node.next, targetNode)
        node.next.next = node
        node.next = None
        return n
#使用recursive方法, 但寫的還不夠直覺
#1.用iteration方式找到頭跟尾
#2.然後reverse頭尾之間的nodes
#3.再把其他node的next指向已經反過來的node list
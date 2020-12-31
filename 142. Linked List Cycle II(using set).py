class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None
#可以簡單的用set或dict找出迴圈的節點
#但空間複雜度為n, 應該用Floyd's 演算法, 空間複雜度降為1
class Solution:
    def addTwoNumbers(self, l1, l2):
        stk1 = []
        stk2 = []
        
        while l1:
            stk1.append(l1)
            l1 = l1.next
        
        while l2:
            stk2.append(l2)
            l2 = l2.next
            
        p = None
        c = 0
        while stk1 or stk2:
            v1 = 0
            if stk1:
                v1 = stk1.pop().val
            v2 = 0
            if stk2:
                v2 = stk2.pop().val
            n = ListNode((v1 + v2 + c) % 10)
            c = (v1 + v2 + c) // 10
            n.next = p
            p = n
        if c == 1:
            n = ListNode(1)
            n.next = p
            p = n
        return p
#因為最低位在list尾端, 所以先用stk把整個list放進去, stk的頂端就會是從最低位開始
#然後再用一個p, 去構建list, 該p指向新的list的頂端
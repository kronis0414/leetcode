class Solution:
    def removeElements(self, head, val):
        p = ListNode(-1)
        p.next = head
        h = p
        pre = p
        cur = p.next
        
        while cur:
            if cur.val == val:
                cur = cur.next
                p.next = cur
            else:
                p = cur
                cur = cur.next
        return h.next
#因為需要考慮有可能移除list的頭, 所以先在list的頭在新增一個Node
#這樣可以避免判斷是否為頭減少程式碼複雜度
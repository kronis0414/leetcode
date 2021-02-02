class Solution:
    def deleteDuplicates(self, head):
        n = ListNode(-1)
        pre_val = -200
        pre = n
        cur = n
        
        while head:
            if head.val == pre_val:
                cur = pre
                cur.next = None
            else:
                #往前
                pre = cur
                cur.next = head
                cur = cur.next
                pre_val = head.val
            head = head.next
        return n.next

#使用2個pointers, cur和pre, 以及一個pre_val, 表示前面的node值
#因為原始list已被排過序, 所以不會出現前面重複node的問題
#只需要一個pre_val紀錄前面的node值
#無論如何只要遇到一個node(head)其值跟前面的node有不同的值(pre_val), 
#則將pre和cur往前, 並設前一個值(pre_val)為head的val
#若遇到相同的node, 則cur退回到pre的位置
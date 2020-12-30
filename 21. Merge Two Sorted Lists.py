class Solution:
    def mergeTwoLists(self, l1, l2):
        ans = ListNode(-1)
        p = ans
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        if l1 != None:
            p.next = l1
        if l2 != None:
            p.next = l2
        return ans.next
#用一個p, 指向新list的尾端
#因為已經排序過, 所以只要依序比大小, 依序改node的next即可
#在最後若其中某個list已經結束, 因為已經排序過只要把剩餘的給p即可
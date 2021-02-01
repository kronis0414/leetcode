class Solution:
    def deleteDuplicates(self, head):
        n = ListNode(-1)
        
        memo = [0] * 201

        while head:
            memo[head.val + 100] += 1
            head = head.next
        p = n
        for i in range(201):
            if memo[i] == 1:
                p.next = ListNode(i - 100)
                p = p.next
        return n.next
#因為node的val被限制在-100到100之間, 所以只要用一個memo去儲存每個val出現次數
#然後再從頭到尾重新產生node即可
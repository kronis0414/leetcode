class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        newHead = Node(head.val)
        p = newHead
        dict = {head:newHead}
        while head is not None:
            #避免把none放入dict
            if head.next and head.next not in dict:
                newNode = Node(head.next.val)
                dict[head.next] = newNode
                p.next = newNode
            elif head.next and head.next in dict:
                p.next = dict[head.next]
            #避免把none放入dict    
            if head.random and head.random not in dict:
                newNode = Node(head.random.val)
                dict[head.random] = newNode
                p.random = newNode
            elif head.random and head.random in dict:
                p.random = dict[head.random]
        
            head = head.next
            p = p.next
        return newHead
#使用一個字典紀錄舊的node和新的node關係
#因為node的val會有重複問題, 所以不能用node的val當作key
#直接從節點的頭到尾iteration, 並用一個指標p指向當前新的node位置
#當遇到尚未處理過的舊節點, 則產生一個val值跟他相同的新節點, 然後建立起舊節點和新節點關係
#無論是next或random都這樣處理
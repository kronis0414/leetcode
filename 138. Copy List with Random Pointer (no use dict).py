class Solution:
    def copyRandomList(self, head):
        if head is None: return None
        
        p = head
        
        while p:
            newNode = Node(p.val)
            newNode.next = p.next
            p.next = newNode
            p = p.next.next
        
        p = head
        
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
            
        newHead = head.next
        p = head
        while p:
            newNode = p.next
            p.next = newNode.next
            #避免在最尾端, 已經沒任何node, 會報錯
            if newNode.next:
                newNode.next = newNode.next.next
            p = p.next
        return newHead
#讓新舊的node彼此之間交叉, 可以不用額外的dict儲存新舊node之間的對應關係
#也就是舊的node若是o1->o2->o3->null
#新節點是n1->n2->n3->null
#第一個while迴圈是把新舊節點交叉合併在一起
#o1->n1->o2->n2->o3->n3->null
#第二個迴圈則是處理random節點, 讓新的節點指向random的新結點, 因為舊節點的random的next指向的新節點, 剛好是目前新節點所要指的random
#比如o3的random節點是o1, 那麼n3也得指向n1
#o1->n1->o2->n2->o3->n3->null
# ^              |
# |---------------
#所以n3的random等於o3的random的next
#第三個迴圈則是把新節點從新舊交叉的節點取出, 舊的不管它
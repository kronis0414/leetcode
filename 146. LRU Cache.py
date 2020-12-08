class ListNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.previous = None
class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.dict = {}
        
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        node.previous.next = node.next
        node.next.previous = node.previous
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        node = None
        if key in self.dict:
            node = self.dict[key] 
            node.val = value
            node.previous.next = node.next
            node.next.previous = node.previous
        else:
            if len(self.dict) == self.size:
                self.dict.pop(self.tail.previous.key)
                n = self.tail.previous
                n.previous.next = n.next
                n.next.previous = n.previous
                del n
            node = ListNode(key, value)
            self.dict[key] = node
        self.moveToHead(node)

    
    def moveToHead(self, node):
        node.previous = self.head
        node.next = self.head.next
        node.next.previous = node
        node.previous.next = node
#宣告一個雙向鏈結串列資料結構
#在LRUCache初始時
#用size保存cache最大儲存大小
#以及head和tail代表該串列結構的頭尾, 新增2個沒用到的node, 分別讓head和tail指向
#這樣做目的是方便以後增加或刪除node
#串列頭表示最近使用的node
#串列尾表示需要被刪除的
#宣告一個字典, 建立key和node之間的關係
#只要有存取到node值, 該node就會被移到最前面, 也就是head的next
#所以把移到最前面的方法獨立出來moveToHead
#需要注意的是
#moveToHead這個方法, node必須從串列裡面獨立出來時才能呼叫
#也就是node的前後之間的node都已經被處理完畢
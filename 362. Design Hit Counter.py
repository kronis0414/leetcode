import queue
class HitCounter:

    def __init__(self):
        self.tmp = queue.deque()

    def hit(self, timestamp):
        self.tmp.append(timestamp)
            
    def getHits(self, timestamp):
        t = timestamp - 299
        
        while self.tmp and self.tmp[0] < t:
            self.tmp.popleft()
        return len(self.tmp)
#使用一個queue保持著300秒以內的值, 無論是在hit或getHits維護queue, 結果都一樣
#在getHits維護queue的話, 則在每次呼叫時, 把超過300秒的元素從queue pop出去
#在hit維護queue的話, 則在每次呼叫時, 則檢查當前進來的timestamp跟最早的timestamp之間的差是否超過300秒

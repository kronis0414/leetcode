class Solution:
    def cloneGraph(self, node):
        if node == None:
            return
        self.seen = {}

        return self.run(node)
    def run(self, node):
        if node.val in self.seen:
            return self.seen[node.val]
        
        newNode = Node(node.val)
        self.seen[node.val] = newNode
        
        for n in node.neighbors:
            neigh = self.run(n)
            newNode.neighbors.append(neigh)
        return newNode
        
#使用遞迴方式
#用一個dict, 去紀錄該node是否處理過(表示對應的新node也建立了), 若處理過則返回
#若沒處理過, 則先建立該node, 並加入dict,
#遞迴該node所有的neighbors
#傳回新的node
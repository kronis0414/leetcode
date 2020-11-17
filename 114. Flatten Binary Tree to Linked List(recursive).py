class Solution:
    def flatten(self, root):
        if root:
            left = self.flatten(root.left)
            right = self.flatten(root.right)
            #將原本節點的左子樹清空
            root.left = None
            #將節點的右子樹設成處理完後的左子樹
            root.right = left
            n = root
            #找到左子樹的葉子
            while n.right != None:
                n = n.right
            #將左子樹的葉子的右節點設成處理完後的右子樹
            n.right = right
            return root
#思路:
#1.把左子樹變成平坦
#2.再把右子樹變成平坦
#3.將根的右子樹設為左子樹
#4.找到原本左子樹的最下面節點, 設為右子樹
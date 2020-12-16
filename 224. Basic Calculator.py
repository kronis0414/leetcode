class Solution:
    def calculate(self, s):
        stk = []
        
        i = 0
        pre = 0
        cur = 0
        op = '+'
        for c in s:
            if c >= '0' and c <= '9':
                cur = cur * 10 + int(c)
            elif c == '(':
                stk.append(pre)
                stk.append(op)
                pre = 0
                cur = 0
                op = '+'
            elif c == ')':
                cur = self.cal(pre, cur, op)
                op = stk.pop()
                pre = stk.pop()
            elif c == '+' or c == '-':
                pre = self.cal(pre, cur, op)
                cur = 0
                op = c
        pre = self.cal(pre, cur, op)
        
        return pre
    def cal(self, v1, v2, op):
        if op == '+':
            return v1 + v2
        else:
            return v1 - v2
#跟227類似
#也是保持著pre, cur, op, 不斷的往運算式的右邊前進
#可以把()想成它就是一個單一的數值, 所以遇到(, 就得先把現在的狀態放入堆疊
#
#首先初始化pre = 0, op=+, 為的是假設前面已經有東西
#當遇到+或-或)時, pre和cur一定有東西, 所以可以運算
#當遇到(時, 只有pre, op有東西, cur沒
#
#當遇到+或-, 就直接運算pre = pre op cur, 並把cur初始為0
#遇到(, 則把現在的pre推入stk, 以及(前的運算子op推入堆疊, 
#遇到), 則先把現在的結果運算完畢, 也就是把()內結果計算出來, 當成cur, 並且pop堆疊裡面的東西 
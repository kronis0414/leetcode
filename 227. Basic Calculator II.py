class Solution:
    def calculate(self, s):
        stk = []
        
        pre = 0
        op = '+'
        cur = 0
        for c in s:
            if c >= '0' and c <= '9':
                cur = cur * 10 + int(c)
            elif c == '+' or c == '-':
                pre = self.cal(pre, cur, op)
                op = c
                cur = 0
            elif c == '*' or c == '/':
                if op == '+' or op == '-':
                    stk.append(pre)
                    pre = cur
                    #為的是A - B * C的減號
                    if op == '-':
                        pre = pre * -1
                    cur = 0
                    op = c
                else:
                    pre = self.cal(pre, cur, op)
                    cur = 0
                    op = c
        pre = self.cal(pre, cur, op)

        while stk:
            pre += stk.pop()
        return pre
                
    def cal(self, v1, v2, op):
        if op == '+':
            return v1 + v2
        elif op == '-':
            return v1 - v2
        elif op == '*':
            return v1 * v2
        elif op == '/':
            return int(v1/v2)
#A + B * C
#A + B + C
#A * B + C

#首先初始化pre = 0, op=+, 為的是假設前面已經有東西
#op代表的是前一個運算子為何
#1.當在計算A + B * C時, 若指標已經在*, 那麼pre = A, op = +, cur = B
#2.當在計算A + B + C時, 若指標已經在第二個+, 那麼pre = A, op = +, cur = B
#3.當在計算A * B + C時, 若指標已經在+, 那麼pre = A, op = *, cur = B
#若現在的運算子c是'+' or '-', 那前面不管是什麼都能夠直接運算, 若前面是優先權高的運算子'*' or '/', 
#那計算不會出問題, 若前面是運算子'+' or '-', 也能先計算, 所以pre = pre op cur
#若現在運算子是'*' or '/', 則還需要判斷前一個運算子是什麼, 若前一個運算子也剛好是'*' or '/', 那也是直接計算, 因為優先權一樣
#否則就需要把目前的pre放入stk裡面, 等待後面最後計算

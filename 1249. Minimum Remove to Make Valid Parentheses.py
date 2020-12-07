class Solution:
    def minRemoveToMakeValid(self, s):
        w = [c for c in s]
        stk = []
        for i, c in enumerate(w):
            if c != '(' and c != ')':
                continue
            if c == '(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                else:
                    w[i] = ''
        while stk:
            w[stk.pop()] = ''
            
        return ''.join(w)
#從左掃到右, 把每個字元當成一個元素放入陣列中
#若只用一個變數去紀錄'('和')'關係, 也就是遇到'('加1, 遇到')'減1
#那麼途中若遇到負的則代表該')'不合法, 但卻無法找出多的'('
#所以用一個stk放'('的索引, 遇到')'則pop一個出來, 表示他們是合法的'()'
#最後stk剩下的'(', 則是多出來的'('
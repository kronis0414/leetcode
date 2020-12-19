class Solution:
    def isValid(self, s):
        stk = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            elif c == ')':
                if not stk or stk.pop() != '(':
                    return False
            elif c == ']':
                if not stk or stk.pop() != '[':
                    return False
            elif c == '}':
                if not stk or stk.pop() != '{':
                    return False
                
        return len(stk) == 0
#因為堆疊先進後出的特性, 和合法的括號組合一樣
#所以用一個堆疊簡單的紀錄左邊的括號, 遇到對應的右括號就pop出來並檢查是否一致
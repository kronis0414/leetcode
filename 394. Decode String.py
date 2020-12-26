class Solution:
    def decodeString(self, s):
        stk = []
        v_stk = []
        k = 0
        
        for c in s:
            if c >= '0' and c <= '9':
                k = k * 10 + int(c)
            elif c == '[':
                stk.append('[')
                v_stk.append(k)
                k = 0
            elif c == ']':
                tmp = []
                times = v_stk.pop()
                
                while stk[-1] != '[':
                    tmp.append(stk.pop())
                stk.pop()
                stk += (tmp[::-1] * times)
            else:
                stk.append(c)
        return ''.join(stk)
#分成2個堆疊, 分別放置字母和次數
#遇到[則把之前的次數推入堆疊裡, 保留起來
#遇到]則把在[之前的字母全部pop出來, 乘上次數, 放入堆疊
#遇到字母放入堆疊
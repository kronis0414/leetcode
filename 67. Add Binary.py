class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        
        c = 0
        tmp = []
        while i >= 0 or j >= 0:
            r = 0
            if i >= 0 and a[i] == '1':
                r += 1
            if j >= 0 and b[j] == '1':
                r += 1
            i -= 1
            j -= 1
            r += c
            c = r // 2
            tmp.append(str(r % 2))
            
        if c == 1:
            tmp.append('1')
            
        return ''.join(tmp[::-1])
        
#跟一般的大整數加總一樣, 只是變成2進制
class Solution:
    def addStrings(self, num1, num2):
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        
        res = []
        c = 0
        while n1 >= 0 and n2 >= 0:
            v1 = ord(num1[n1]) - 0x30
            v2 = ord(num2[n2]) - 0x30
            v = v1 + v2 + c
            c = v // 10
            v = v % 10
            res.append(str(v))
            n1 -= 1
            n2 -= 1
            
        for i in range(n1, -1, -1):
            v = ord(num1[i]) - 0x30 + c
            c = v // 10
            v = v % 10
            res.append(str(v))
        for i in range(n2, -1, -1):
            v = ord(num2[i]) - 0x30 + c
            c = v // 10
            v = v % 10
            res.append(str(v))
        if c != 0:
            res.append(str(1))
        return ''.join(res[::-1])
#很簡單
#但要注意的是進位問題即可
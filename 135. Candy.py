class Solution:
    def candy(self, ratings):
        n = len(ratings)
        tmp1 = [0] * n
        tmp2 = [0] * n

        tmp1[0] = 1
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                tmp1[i] = tmp1[i-1] + 1
            else:
                tmp1[i] = 1

        tmp2[-1] = 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                tmp2[i] = tmp2[i+1] + 1
            else:
                tmp2[i] = 1
        s = 0
        for i in range(n):
            s += max(tmp1[i], tmp2[i])
        return s
#宣告2個array, 分別是從左到右, 和從右到左, 所需要的candy數
#若左邊的元素(i-1)rating比目前(i)的大, 那麼目前(i)所需要的candy數為左邊+1, 反之
#最後, 全部所需的candy數, 則是取2者最大值
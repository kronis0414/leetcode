import collections
class Solution:
    def numPairsDivisibleBy60(self, time):
        memo = collections.defaultdict(int)
        ans = 0
        for t in time:
            if 60 - t % 60 in memo:
                ans += memo[60 - t % 60]
            if t % 60 == 0:
                memo[60] += 1
            else:
                memo[t % 60] += 1
            
        return ans
#很明顯得用一個dict去儲存過去的值, 才能達到O(n)的運算速度
#因為(a + b) mod 60 = a mod 60 + b mod 60, 利用這個特性, 去dict找剩下的餘數是否存在
#又因為重複出現的time也要計算, 所以得累積相同的餘數次數
#比如[60,60,60]
#第一個60和第二個60
#第一個60和第三個60
#第二個60和第三個60
#又若t能被60整除, 則餘數會得0, 60 - t % 60會得到60, 會找不到答案
#所以得在dict存放60
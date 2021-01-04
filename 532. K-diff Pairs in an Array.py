import collections
class Solution:
    def findPairs(self, nums, k):
        memo = collections.defaultdict(int)
        for n in nums:
            memo[n] += 1
    
        seen = set()
        ans = 0
        for n in nums:
            memo[n] -= 1
            diff = n - k
            pair = [diff, n]
            pair.sort()
            pair = tuple(pair)
            if diff in memo and memo[diff] > 0 and pair not in seen:
                seen.add(pair)
                ans += 1
            memo[n] += 1
        return ans
#因為會有重複的元素, 但又要求unique pair, 所以得用seen去紀錄是否存在相同的pair
#且也必須考慮k = 0情況下, 所以得紀錄每個元素出現個數
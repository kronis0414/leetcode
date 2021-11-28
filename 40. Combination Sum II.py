class Solution:
    def combinationSum2(self, candidates, target):
        countArray = [0] * 51
        for v in candidates:
            countArray[v] += 1
        oneAns = []
        ans = []
        def run(v, start_i):
            if v == 0:
                ans.append(oneAns.copy())
                return
            for i in range(start_i, 51):
                if v - i < 0:
                    break
                if countArray[i] > 0:
                    oneAns.append(i)
                    countArray[i] -= 1
                    run(v - i, i)
                    oneAns.pop()
                    countArray[i] += 1
        run(target, 1)
        return ans
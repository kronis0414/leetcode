import queue
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        memo = {}
        
        for w in wordList:
            for i in range(len(w)):
                k = w[:i] + '_' + w[i+1:]
                if k in memo:
                    memo[k].append(w)
                else:
                    memo[k] = [w]
                    
        q = queue.deque()
        q.append(beginWord)
        step = 1
        seen = set([beginWord])
        while q:
            l = len(q)
            #這次階層有多少個word必須被處理
            for i in range(l):
                word = q.popleft()
                if word == endWord:
                    return step
                for j in range(len(word)):
                    #
                    kw = word[:j] + '_' + word[j+1:]
                    if kw in memo:
                        for w in memo[kw]:
                            if w not in seen:
                                q.append(w)
                                seen.add(w)
            step += 1
        return 0
#用bfs, 能找到從beginWord變成endWord最短長度
#用一個memo把wordList裡面的word歸類
#例如
#把hot, dot, 放在_ot裡
#把dot, dog, 放在do_裡
#以此類推
#從beginWord開始, 把每個在beginWord的字元用_代替後, 找找看是否存在在memo裡
#例如beginWord = hit, 則會有_it, h_t, hi_, 這三種變化
#若存在在memo裡, 則把對應的memo裡面的words都丟入候選q, 並且記錄那些word已經用過,
#用過的word不能加入候選, 避免陷入無限循環, 抓取候選代表每次只變化一個字元, 符合題目規定
#一直不斷用處理beginWord方式處理這些候選word, 得到答案
#因為使用bfs概念, 所以從q取出來的word, 若等於endWord, 那就表示遇到答案
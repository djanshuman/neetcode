from collections import defaultdict , deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Edge Case
        if endWord not in wordList:
            return 0
        
        # Adjacency list to store pattern : words
        nei = defaultdict(list)
        # Add begin word because we need to find all patterns for all word
        wordList.append(beginWord)

        # Seeding, generate all patterns and store in defaultDict (List)
        '''
        defaultdict(<class 'list'>, {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot', 'hit'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog'], '*it': ['hit'], 'hi*': ['hit']})
        '''
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)
        
        # Perform BFS , take out all words for a pattern , traverse level by level
        q = deque([beginWord])
        visited =set([beginWord])
        res = 1
        while q:
            lenq = len(q)
            for _ in range(lenq):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for patternWord in nei[pattern]:
                        if patternWord in visited:
                            continue
                        visited.add(patternWord)
                        q.append(patternWord)
            res += 1
        return 0
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        
        #base
        dp[n] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                end = i + len(w)
                if end <= len(s) and s[i : end] == w and dp[end]: #Why explanation below. If code is matched, its first part,start from end which is empty string is second word & can be formed, that is what it guarantees here. So  dp[4] -> relies on dp[8], dp[0] -> dp[4]
                    dp[i] = True
                    break
    
        return dp[0]


'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


'''


'''
Why dp[end] and not something else: if word w occupies s[i : end], then the next decision starts at index end. The segmentability of "the rest" is precisely dp[end]. The base case dp[n] = True is what makes a word that reaches the very end succeed — end == n, so dp[end] = dp[n] = True.

Trace s = "leetcode", dict {leet, code} (indices l=0,e=1,e=2,t=3,c=4,o=5,d=6,e=7, n=8):

i	word that matches	end	dp[end]	dp[i]
8	(base)	—	—	True
7..4	none match at 7,6,5	—	—	False
4	code (s[4:8])	8	dp[8]=True	True
3..1	none start here	—	—	False
0	leet (s[0:4])	4	dp[4]=True	True

dp[0] = True → "leetcode" segments into leet + code. ✓

Notice the chain: dp[0] is True only because dp[4] was True, which was True only because dp[8] (the base) was True. Each dp[end] reaches back to confirm the remainder — that's the whole mechanism. Match a word, then trust dp[end] to vouch for the rest.
'''
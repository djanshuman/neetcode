class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up with Memo
        '''
        The "start at 1, subtract 1" pairing is the thing to lock in for every prefix-length two-string DP. They always come together:

        Table sized (n+1) × (m+1) → row/col 0 is the empty-prefix base case
        Loops run range(1, n+1) and range(1, m+1) → skip the base case, fill the rest
        Character lookups text1[i-1], text2[j-1] → convert prefix-length back to string index   
        '''
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        # Initialization
        for i in range(m + 1):
            dp[0][i] = 0
        
        for j in range(n + 1):
            dp[j][0] = 0

        #Base case

        for i in range(1, n + 1):
            for j in range(1,m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i -1][j] , dp[i][j -1])
        
        return dp[n][m]



'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down with Memo
        
        #LCS done, memoized and verified. You've now got the two-string DP pattern #locked in: match → 1 + diag, mismatch → max(drop-from-A, drop-from-B), #base case at any negative index → 0.
        
        def generate_lcs(n, m,dp):


            if n < 0 or m < 0:
                return 0

            if dp[n][m] != -1:
                return dp[n][m]

            if text1[n] == text2[m]:
                dp[n][m] = 1 + (generate_lcs(n - 1,m - 1,dp))
            else:
                dp[n][m] = max(generate_lcs(n -1,m,dp) , generate_lcs(n,m - 1,dp))
        
            return dp[n][m]

        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return generate_lcs(n - 1, m - 1,dp)
        
'''


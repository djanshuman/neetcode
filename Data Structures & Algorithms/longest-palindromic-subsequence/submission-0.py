class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # reverse it to create s2 , common characters are palindrome as reverse and non-reverse
        # a palindromic subsequence of s is exactly a subsequence common to s and its reverse
        s1 = s
        s2 = s1[::-1]
        
        n = len(s1)
        m = n
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] =  1 + dp[i -1][j - 1]
                else:
                    dp[i][j] = max(dp[i -1][j] , dp[i][j - 1])

        return dp[n][m]
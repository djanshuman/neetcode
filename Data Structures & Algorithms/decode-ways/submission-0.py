class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1
        
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            pick = dp[i + 1] 
            if i + 1 < n and (10 <= int(s[i : i + 2]) <= 26):
                pick += dp[i + 2]  
            dp[i] = pick
        return dp[0]


'''
class Solution:
    def numDecodings(self, s: str) -> int:

        def generate_sequence(idx):
            if idx == n:
                return 1

            if s[idx] == "0":
                return 0

            if dp[idx] != -1:
                return dp[idx]

            pick = generate_sequence(idx + 1)  # Slice [0 : 1], take 1st digit
            # to take entire string with second validate if within bound and 10 - 26
            if idx + 1 < n and (10 <= int(s[idx : idx + 2]) <= 26):
                pick += generate_sequence(
                    idx + 2
                )  # slic [ 0 :  2] take 0 and 1 index together
            dp[idx] = pick
            return dp[idx]

        n = len(s)
        dp = [-1] * (n + 1)
        return generate_sequence(0)
'''
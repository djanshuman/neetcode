class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = 1
        second = 1

        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return second


'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
'''
        
'''
class Solution:
    def climbStairs(self, n: int) -> int:

        def calc_stairs(idx):
            if idx == 0:
                return 1

            if idx == 1:
                return 1

            if dp[idx] != -1:
                return dp[idx]

            dp[idx] = calc_stairs(idx - 1) + calc_stairs(idx - 2)
            return dp[idx]

        dp = [-1] * (n + 1)
        return calc_stairs(n)
'''
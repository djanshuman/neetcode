class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def calc_cost(cost, n):
            if n <= 1:
                return 0 
            
            if dp[n] != -1:
                return dp[n]
            
            dp[0] = dp[1] = 0

            dp[n] = min(
                    calc_cost(cost, n-1) + cost[n-1], 
                    calc_cost(cost, n-2) + cost[n-2]
                )
            return dp[n]

        n = len(cost)
        dp = [-1] * (n + 1)
        return calc_cost(cost, n)
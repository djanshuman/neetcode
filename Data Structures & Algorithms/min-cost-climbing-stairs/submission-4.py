class Solution:
    '''
The lesson, and it's the same shape as the House Robber base-case bug an hour ago: when the problem gives you more than one free starting point, each of those points needs its own base case. Here steps 0 and 1 are both free entries, so both need a base that returns just their own cost.
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        def min_cost(idx):
            if idx < 0:
                return float('infinity')
            
            if idx <= 1:
                return cost[idx]

            if dp[idx] != -1:
                return dp[idx]

            one_step = cost[idx] + min_cost(idx - 1)
            two_step = cost[idx] +  min_cost(idx - 2)
            dp[idx] = min(one_step , two_step)
            return dp[idx]

        n = len(cost)
        dp = [-1] * (n + 1)
        return min(min_cost(n - 1), min_cost(n - 2))


'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def calc_cost(cost, n):
            if n <= 1:
                return 0 
            
            if dp[n] != -1:
                return dp[n]
   
            dp[n] = min(
                    calc_cost(cost, n-1) + cost[n-1], 
                    calc_cost(cost, n-2) + cost[n-2]
                )
    
            return dp[n]

        n = len(cost)
        dp = [-1] * (n + 1)
        return calc_cost(cost, n)
'''
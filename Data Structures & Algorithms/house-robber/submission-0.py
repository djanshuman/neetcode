class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialization
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        #base initialization
        robber_1 = nums[0]
        robber_2 = max(nums[0], nums[1])

        for i in range(2,n):
            third_robber = max(robber_2, nums[i] + robber_1)
            robber_1, robber_2 = robber_2, third_robber
        return third_robber
'''
    def rob(self, nums: List[int]) -> int:
        # INITIALIZATION BASE CASE
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        #USING EXTRA MEMORY
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n ):
            dp[i] = max(dp[i - 1] , dp[i - 2] + nums[i])
        return dp[-1]

'''
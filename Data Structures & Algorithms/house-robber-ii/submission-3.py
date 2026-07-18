class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robber(nums[1:]),self.robber(nums[:-1]))


    def robber(self, nums: List[int]) -> int:
        # bottom up with space optimisation
        n = len(nums)
        if n == 0:
            return 0
            
        first = 0
        second = nums[0]

        for i in range(1, n):
            take = nums[i]
            if i >= 2:
                take += first
            not_take = 0 + second

            third = max(take,not_take)
            first = second
            second = third

        return second
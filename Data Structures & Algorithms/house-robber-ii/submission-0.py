class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robber(nums[1:]),self.robber(nums[:-1]))

    def robber(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        first_robber = nums[0]
        second_robber = max(nums[0], nums[1])
        for i in range(2,n):
            third_robber = max(second_robber, first_robber + nums[i])
            first_robber,second_robber = second_robber, third_robber
        return third_robber

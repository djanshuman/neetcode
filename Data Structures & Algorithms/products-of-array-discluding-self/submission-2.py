class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [0] * len(nums)

        prefix = 1
        for r in range(len(nums)):
            res[r] = prefix
            prefix *= nums[r]

        postfix = 1

        for r in range(len(nums) - 1,  -1,  -1):
            res[r]*= postfix
            postfix *= nums[r]

        return res
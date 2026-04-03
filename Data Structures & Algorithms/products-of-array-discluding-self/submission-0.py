class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = [0] * len(nums)
        prefix = 1

        # prefix calculation O(n)
        for i in range(len(nums)):
            result_list[i] = prefix
            prefix = prefix * nums[i]

        # postfix calculation # [1, 1, 2, 6]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            temp = result_list[j]
            result_list[j] = postfix * temp
            postfix = nums[j] * postfix
        return result_list
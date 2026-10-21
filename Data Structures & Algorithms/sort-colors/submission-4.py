class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            ele = nums[i]

            if ele == 0:
                nums[l], nums[i] = nums[i] , nums[l]
                l += 1

            elif ele == 2:
                nums[r], nums[i] = nums[i] , nums[r]
                r -= 1
                i -=1

            i += 1

        return nums
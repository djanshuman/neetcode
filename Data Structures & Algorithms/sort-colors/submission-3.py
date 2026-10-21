class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i,j):
            nums[i], nums[j] = nums[j] , nums[i]
        
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            ele = nums[i]

            if ele == 0:
                swap(l,i)
                l += 1

            elif ele == 2:
                swap(r,i)
                r -= 1
                i -=1

            i += 1

        return nums

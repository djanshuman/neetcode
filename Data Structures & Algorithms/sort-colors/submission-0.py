class Solution:
    
    def swap(self,i,j,nums):
        nums[i] , nums[j] = nums[j] , nums[i]
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Declare pointers , i is the third pointer which will scan and look out for 0 or 2
        l , r = 0 , len(nums) - 1
        i = 0

        # Run two pointer logic
        while i <= r:
            if nums[i] == 0:
                self.swap(l,i,nums)
                l += 1

            elif nums[i] == 2:
                self.swap(r, i,nums)
                r -= 1
                i -= 1
            i += 1


        

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
        # Logic is to keep all 0 to left , 1 in middle and 2 in right. 
        # whenever i scans and find value, swap it. 
        while i <= r:
            if nums[i] == 0:
                self.swap(l,i,nums)
                l += 1

            elif nums[i] == 2:
                self.swap(r, i,nums)
                r -= 1
                i -= 1       # edge case, whenever we swap with r, 
                             # we shouldn't move i pointer, because if we swap 0 and 2 , then 0 is introduced in middle and i moves ahead.
                             # to counter the -ve , +ve with outer i as it will run each time, we decrement it.
            i += 1



'''
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l, i = 0, 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                # Swap current 0 with the 'l' pointer
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1  # We can move i because we know what came from l (it's either a 0 or 1)
            elif nums[i] == 2:
                # Swap current 2 with the 'r' pointer
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                # DO NOT increment i here; we need to re-scan the new nums[i]
            else:
                # It's a 1, just leave it in the middle and move on
                i += 1
'''
        

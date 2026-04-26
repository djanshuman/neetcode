class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            # Skip the same value for the first element to avoid duplicate triplets
            if i > 0 and a == nums[i-1]:
                continue

            if a > 0:
                break

            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second element
                    # Note: We check l < r first for safety!
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                    # Note: We don't strictly need to skip duplicates for 'r' 
                    # because the sum logic will naturally force 'r' to move 
                    # in the next iterations, but it doesn't hurt.
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
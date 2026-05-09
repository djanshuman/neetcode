class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxlen = 0
        # Instead of a full dictionary, we only need to count zeros
        zeros_count = 0 

        for r in range(len(nums)):
            # 1. Expand: If we see a 0, it costs us 1 from our 'k' budget
            if nums[r] == 0:
                zeros_count += 1

            # 2. Validate: If zeros exceed k, we must shrink from the left
            while zeros_count > k:
                if nums[l] == 0:
                    zeros_count -= 1
                l += 1

            # 3. Update: Record the longest valid window
            maxlen = max(maxlen, r - l + 1)
            
        return maxlen
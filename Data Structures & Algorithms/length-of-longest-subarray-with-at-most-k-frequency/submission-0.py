class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_len = float('-inf')
        freq = dict()
        l = 0
  
        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r],0) + 1
         
            while freq[nums[r]] > k:
                left = nums[l]
                freq[left] -=1
                if freq[left] == 0:
                    del freq[left]
                l += 1
     
            max_len = max(max_len,r - l + 1)
        
        return max_len

    

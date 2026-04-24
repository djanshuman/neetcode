class Solution:
    
    # Helper function to check if we can split the array into subArray to check the MID value which is the Sum.
    
    def feasible_solution(self, maxsum , nums, k):
        no_of_subArray = 0
        curr_sum = 0

        for i in nums:
             curr_sum += i
             if curr_sum > maxsum:
                no_of_subArray += 1
                curr_sum = i

        '''Here we do + 1 , because if we can achieve the sum with less number of subarray <= k, then we can just split one of array
            to match K. no_of_subArray without + 1 is also a feasible solution, splitting it one more time will meet result.
        '''

        return no_of_subArray + 1 <= k      #+1 counts the last subarray
        
    
    def splitArray(self, nums: List[int], k: int) -> int:
        l  = max(nums) # minimum sum we can achieve is the largest value in nums.  min possible largest sum = biggest element
        r = sum(nums)  # maximum sum we can achieve is the sum of all values in nums. max possible = take all in one subarray
        
        res = r # maximum sum we can have in total for nums .
                #There's always a valid answer here — worst case is k=1 which means sum(nums). So initializing res = r = sum(nums) is safe.

        while l <= r:
            mid = (l + r) // 2

            if self.feasible_solution(mid,nums,k):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

        
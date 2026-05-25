class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # step 1: initialize variables.
        min_dq = deque() # Store minimum element
        max_dq = deque() # Store maximum element
        l = r = 0
        resLen = 0
        ''' In this problem we need to utilise two deques and check
        different between max and min is <= limit , if window is invalid , shrink left
        and if anytime top of deque is outside current window, popleft them.
        Then update the state outside while loop to record max length of subarray.
        '''

        # step 2 : traverse and record elements

        for r in range(len(nums)):

            # step 3: minimum deque operations
            while min_dq and nums[min_dq[-1]] > nums[r]:
                min_dq.pop()
            min_dq.append(r)

            # step 4 : max deque operations
            while max_dq and nums[max_dq[-1]] < nums[r]:
                max_dq.pop()
            max_dq.append(r)

            # step 5: check for invalid window and shrink
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                l += 1
                # if max or min element fell out of window, remove them
                if min_dq[0] < l:
                    min_dq.popleft()

                if max_dq[0] < l:
                    max_dq.popleft()
            # step 6: record the result , longest subarray length
            resLen = max(resLen,r - l + 1)

        return resLen


'''
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque() # monotonically increasing
        max_q = deque() # monotonically decreasing
        reslen = 0
        l = 0

        for r , n in enumerate(nums):

            while min_q and min_q[-1] > n:
                min_q.pop()

            while max_q and max_q[-1] < n:
                max_q.pop()

            min_q.append(n)
            max_q.append(n)

            while max_q[0] - min_q[0] > limit:
                
                if nums[l] == max_q[0]:
                    max_q.popleft()
                
                if nums[l] == min_q[0]:
                    min_q.popleft()
                
                l += 1

            reslen = max(reslen, r - l + 1)
        return reslen


'''




        

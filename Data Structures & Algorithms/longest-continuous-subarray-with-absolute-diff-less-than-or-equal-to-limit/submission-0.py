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



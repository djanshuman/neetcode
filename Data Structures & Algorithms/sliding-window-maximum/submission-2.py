'''
efficient solution is using a deque because add/remove from both sides is O(1)
rules:
1. If front of queue is outside window, evict it
2. If top of is lower than entering element, evict it
3. if my window is full, record the result

we are maintaining a monotonic decreasing queue, where first element is always bigger
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []

        for i , n in enumerate(nums):

            while dq and dq[0] < i - k + 1:
                dq.popleft()


            while dq and nums[dq[-1]] < n:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # monotonically decreasing
        res = []

        for i , n in enumerate(nums):
            # 1. Front eviction — remove indices outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. Back eviction — remove weaker candidates
            while dq and nums[dq[-1]] < n:
                dq.pop()
            
            # 3. Append after restructuring
            dq.append(i)

            # 4. Record result once window is full
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat element as index position and assign pointers
        # similar to slow and fast as head
        # Phase 1 logic - Find if cycle exist

        slow = nums[0]
        fast = nums[0]

        #Phase 1 , find the meeting point , cycle point. As per question, the soln is guaranteed so we use while True
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #Phase 2 , find the entry point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        

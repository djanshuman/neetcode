# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break
        
        if has_cycle:
            return True
        return False
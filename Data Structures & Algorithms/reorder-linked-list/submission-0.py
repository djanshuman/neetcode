# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1 - find middle of linked List

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2 - define starting of second half and reverse it
        second = slow.next
        before = slow.next = None
        while second:
            after = second.next
            second.next = before
            before = second
            second = after
        
        # Step 3 - Merging and repointing to take alternate elements from 1st half -> second half
        first , last = head, before
        while last:
            temp1 = first.next
            temp2 = last.next
            
            first.next = last
            last.next = temp1
            first = temp1
            last = temp2
        
            
        
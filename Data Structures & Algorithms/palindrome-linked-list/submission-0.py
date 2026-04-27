# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1 - Find Middle of Linked List or Middle Node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2 - Reverse the second half of the LinkedList
        before = None
        curr = slow
        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        
        # Step 3 - Perform palindrome check using twoPointer Logic
        l , r = head, before
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True

          
        
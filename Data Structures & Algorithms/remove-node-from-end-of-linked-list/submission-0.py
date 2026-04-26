# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # validate inputs
        if head is None or n < 1:
            return head


        # creating a dummy Node to point head and fast
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy

        #traverse fast n steps ahead. In case n > len(list) then default return head as last element possible to delete from end.
        for _ in range(n):
            if fast.next is None:
                return head
            fast = fast.next
        
        #Now assign slow to dummy and move both pointers till fast reaches end.
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next

        #End of loop, slow is exactly 1 position behind the element to be deleted, swap pointers and remove in-place.
        slow.next = slow.next.next

        #Return head of LL.
        return dummy.next


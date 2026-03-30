# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr:
            next_ptr = curr.next
            curr.next = None
            prev_ptr = curr
        while curr and next_ptr:
            curr = next_ptr
            next_ptr = curr.next
            curr.next = prev_ptr
            prev_ptr=curr
        return curr
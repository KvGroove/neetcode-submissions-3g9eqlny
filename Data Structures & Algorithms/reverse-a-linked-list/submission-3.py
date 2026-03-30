# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next_node = curr.next # Store next node
            curr.next = prev # Reassign next pointer
            prev = curr # Store pointer for next iteration
            curr = next_node # Go to next iteration
        return prev
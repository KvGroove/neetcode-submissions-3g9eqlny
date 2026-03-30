# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.mergeHelper(lists, 0, len(lists) - 1)

    def mergeHelper(self, lists: List[Optional[ListNode]], s, e) -> Optional[ListNode]:
        if s >= e:
            return lists[s]

        m = (s + e) // 2
        left = self.mergeHelper(lists, s, m)
        right = self.mergeHelper(lists, m + 1, e)

        return self.merge(left, right)

    def merge(self, left, right) -> Optional[ListNode]:
        if left is None:
            return right
        if right is None:
            return left
        
        if left.val <= right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        
        curr = head
        while left and right:
            if left.val <= right.val:
                curr.next = left
                curr = curr.next
                left = left.next
            else:
                curr.next = right
                curr = curr.next
                right = right.next
        
        if left is None:
            curr.next = right
        if right is None:
            curr.next = left

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-1)
        large = ListNode(-1)
        small_head = small
        large_head = large
        
        while head:
            
            if head.val < x:
                small.next = head
                head = head.next
                small = small.next
                small.next = None
            
            else:
                large.next = head
                head = head.next
                large = large.next
                large.next = None
        
        small.next = large_head.next
        
        return small_head.next
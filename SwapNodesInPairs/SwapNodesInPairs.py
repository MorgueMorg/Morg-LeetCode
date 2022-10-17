# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head
        curr = node
        while curr.next is not None and curr.next.next is not None:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            curr.next = second
            curr.next.next = first
            curr = curr.next.next
        return node.next
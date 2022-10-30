# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1 
        cur.next = head

        k = length - (k % length)
        while k > 0:
            cur=cur.next
            k -= 1

        newhead = cur.next
        cur.next = None
        return newhead
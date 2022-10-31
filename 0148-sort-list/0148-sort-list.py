# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        arr.sort()
        dummy=curr=ListNode(0)
        
        for i in arr:
            temp=ListNode(i)
            curr.next=temp
            curr=curr.next
        return dummy.next
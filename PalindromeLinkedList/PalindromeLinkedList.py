# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = middle = head
        reverse = None

        while fast and fast.next:
            fast = fast.next.next
            current, middle = middle, middle.next
            current.next, reverse = reverse, current

        if fast:
            middle = middle.next

        while reverse:
            if reverse.val != middle.val:
                return False
            reverse = reverse.next
            middle = middle.next

        return True
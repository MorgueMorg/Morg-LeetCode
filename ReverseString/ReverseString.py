class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse
        """
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Two Pointers
        """
        pointer1 = 0
        pointer2 = len(s) - 1
        while pointer1 < pointer2:
            s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
            pointer1 += 1
            pointer2 -= 1


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Recursion
        """
        def helper( left, right, string):                 
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper( left+1, right-1, s)
        helper( left = 0, right = len(s)-1, string = s)
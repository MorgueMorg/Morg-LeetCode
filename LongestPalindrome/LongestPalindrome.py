class Solution:
    def longestPalindrome(self, s: str) -> int:
        hasht = set()
        for i in s:
            if i not in hasht:
                hasht.add(i)
            else:
                hasht.remove(i)
        return len(s) - len(hasht) + 1 if len(hasht) > 1 else len(s)
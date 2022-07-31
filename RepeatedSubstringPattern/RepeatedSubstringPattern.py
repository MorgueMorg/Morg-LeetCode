class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1 : -1]


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0 and s[:i] * (length // i) == s:
                return True
        return False

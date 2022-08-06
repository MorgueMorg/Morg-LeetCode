class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                prev, cur = cur, 1
            if cur <= prev:
                res += 1
        return res
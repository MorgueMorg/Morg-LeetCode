class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        upper, lower = ord("Z"), ord("z")
        for i in range(26):
            if chr(upper - i) in s and chr(lower - i) in s:
                return chr(upper - i)
        return ""
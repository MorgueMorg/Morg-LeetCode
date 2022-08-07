class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n+32) if n > 64 and n < 91 else c
        return ans


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)
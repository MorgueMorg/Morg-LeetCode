class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in set(t):
            if s.count(i) != t.count(i): return i


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for i, j in enumerate(s):
            if j != t[i]: return t[i]
        return t[-1]


# ! Побитовый метод
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for c in s+t:
            x ^= ord(c)
        return chr(x)
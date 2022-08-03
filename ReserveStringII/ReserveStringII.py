class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
        return "".join(s)
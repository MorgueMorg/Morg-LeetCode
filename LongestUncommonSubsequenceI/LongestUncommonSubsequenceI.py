class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        return max(len(a), len(b))


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        l=[a[i:] for i in range(len(a))]
        for i in l:
            if i != b:
                return len(i) if len(i)>len(b) else len(b)
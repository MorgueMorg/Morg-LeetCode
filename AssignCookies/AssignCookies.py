class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        count, i, j = 0,0,0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                count+=1
                i+=1
                j+=1
            else:
                i+=1
        return count


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j in range(len(s)):
            if i < len(g) and g[i] <= s[j]:
                i += 1
        return i
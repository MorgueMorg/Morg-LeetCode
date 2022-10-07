class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        ind = s.index(c)
        for i in range(len(s)):
            if abs(ind-i)>abs(s.find(c,i)-i):
                ind = s.index(c,i)
            if s[i]!=c:
                ans.append(abs(ind-i))
            else:
                ans.append(0)
        return ans
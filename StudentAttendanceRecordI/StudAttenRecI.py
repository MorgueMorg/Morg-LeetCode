class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") <= 1 and s.count("LLL") == 0: return True
        return False


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") <= 1 and s.count("LLL") == 0


class Solution:
    def checkRecord(self, s: str) -> bool:
        d=0
        for i in range(len(s)):
            if s[i]=='A':
                d+=1
            if d==2:
                return False
            if i>=2 and s[i]==s[i-1]==s[i-2]=='L':
                return False
        return True


class Solution:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        for l in s:
            if l == 'A': A += 1
            elif l == 'L': L += 1
            if l != 'L': L = 0
            if L > 2 or A > 1: return False
        return True
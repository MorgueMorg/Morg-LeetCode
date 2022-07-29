class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for i in t:
            if counter == len(s):
                break
            elif s[counter] == i:
                counter += 1
        return counter == len(s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j  = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
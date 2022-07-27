class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = Counter(s)
        for i, char in enumerate(s):
            if dict[char] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1
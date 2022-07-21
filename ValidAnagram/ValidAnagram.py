class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1, dct2 = {}, {}
        for i in s:
            dct1[i] = dct1.get(i, 0) + 1
        for i in t:
            dct2[i] = dct2.get(i, 0) + 1
        return dct1 == dct2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
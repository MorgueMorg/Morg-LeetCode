class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        hasht = {}
        for i in range(len(t)):
            if t[i] not in hasht:
                hasht[t[i]] = s[i]
            elif hasht[t[i]] != s[i]:
                return False
        return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct1, dct2 = {}, {}
        for i, val in enumerate(s):
            dct1[val] = dct1.get(val, []) + [i]
        for i, val in enumerate(t):
            dct2[val] = dct2.get(val, []) + [i]
        return sorted(dct1.values()) == sorted(dct2.values())


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = s.count(i) 
            d=dic[s[0]]
            for i, j in enumerate(dic):
                if dic[j] != d:
                    return False
        return True
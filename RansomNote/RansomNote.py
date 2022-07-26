class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = dict(Counter(ransomNote))
        dict2 = dict(Counter(magazine))
        for i in dict1 :
            if not i in dict2 :
                return False
            else:
                if dict1[i] > dict2[i] :
                    return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
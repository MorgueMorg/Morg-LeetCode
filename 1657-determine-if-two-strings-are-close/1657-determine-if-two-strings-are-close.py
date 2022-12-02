class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        has1 = set(word1)
        has2 = set(word2)       
        countOne = Counter(word1)
        countTwo = Counter(word2)     
        if sorted(countOne.values()) == sorted(countTwo.values()) and has1 == has2:
                return True
        return False
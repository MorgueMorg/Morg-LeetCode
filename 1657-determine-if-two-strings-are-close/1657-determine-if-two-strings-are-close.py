class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        has1, has2 = set(word1), set(word2)       
        countOne, countTwo = Counter(word1), Counter(word2)
        if sorted(countOne.values()) == sorted(countTwo.values()) and has1 == has2:
                return True
        return False
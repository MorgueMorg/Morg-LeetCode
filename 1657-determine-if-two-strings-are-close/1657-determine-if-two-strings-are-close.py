class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:      
        if sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2): return True
        return False
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        l = len(s) + 1 
        a, b = s[0:l // 2], s[l // 2:]
        countA = sum(i in vowels for i in a)
        countB = sum(i in vowels for i in b)
        return countA == countB
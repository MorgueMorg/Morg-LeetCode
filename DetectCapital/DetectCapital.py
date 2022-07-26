class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2: return True
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower():
                    return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
        return True


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return len(word) <= 1 or max(word) <= 'Z' or min(word[1:]) >= 'a'


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper(): return True
        if word.islower(): return True
        if word[0].isupper() and word[1:].islower(): return True
        return False
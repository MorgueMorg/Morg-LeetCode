class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = "".join(letter.lower() for letter in licensePlate if letter.isalpha())
        # sort words by length.
        words.sort(key = len)
        for word in words:
            check = True
            for ch in set(licensePlate):
                if ch not in word or licensePlate.count(ch) > word.count(ch):
                    check = False
                    break
            if check == True:
                return word
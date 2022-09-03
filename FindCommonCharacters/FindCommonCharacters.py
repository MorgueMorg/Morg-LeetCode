class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict_ = {}
        for c in set(words[0]):
            dict_[c] = min([word.count(c) for word in words])
        arr = []
        for key, value in dict_.items():
            if value > 0:
                for _ in range(value):
                    arr.append(key)
        return arr
        
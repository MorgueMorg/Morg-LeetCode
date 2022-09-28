class Solution:
    def sortSentence(self, s: str) -> str:
        split_ = s[::-1].split(" ")
        split_ = sorted(split_)
        res = []
        for i in split_:
            res.append(i[1:][::-1])
        return " ".join(res)
            
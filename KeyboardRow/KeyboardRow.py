class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for i in words:
            if set(i.lower()) <= row1:
                arr.append(i)
            elif set(i.lower()) <= row2:
                arr.append(i)
            elif set(i.lower()) <= row3:
                arr.append(i)
        return arr


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        arr = []
        for word in words:
            w = set(word.lower())
            if w <= row1 or w <= row2 or w <= row3:
                arr.append(word)
        return arr


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        return [w for w in words if any(s&set(w.lower())==set(w.lower()) for s in rows)]


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [x for x in words if set(x).issubset(set("qwertyuiopQWERTYUIOP")) or set(x).issubset(set("asdfghjklASDFGHJKL")) or set(x).issubset(set("zxcvbnmZXCVBNM")) ]
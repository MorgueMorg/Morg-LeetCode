class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = []
        for i in s:
            if "|" not in arr:
                arr.append(i)
            elif "|" in arr and i == "|":
                arr.pop()
        return arr.count("*")
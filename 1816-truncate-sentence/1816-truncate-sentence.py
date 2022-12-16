class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = list(s.split())
        while len(arr) != k:
            arr.pop()
        return " ".join(arr)
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            count = i.count(" ")
            ans = max(ans, count)
        return ans + 1
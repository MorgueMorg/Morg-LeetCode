class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
        res = ""
        for i in sorted_count:
            res += i[0] * i[1]
        return res
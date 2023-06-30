class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            s = str(i)
            if "0" in s:
                continue
            d = 1
            for j in range(len(s)):
                if i % int(s[j]) != 0:
                    d = 0
                    break
            if d == 1:
                res.append(i)
        return res
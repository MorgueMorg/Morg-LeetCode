class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        curr = (2 * numRows) - 2
        res = ""
        for i in range(numRows):
            j = 0
            while i + j < len(s):   
                res += s[j + i]
                sec = (j - i) + curr
                if i != 0 and i != numRows - 1 and sec < len(s):
                    res += s[sec]
                j += curr
        return res
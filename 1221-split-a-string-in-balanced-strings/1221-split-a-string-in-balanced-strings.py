class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = countL = 0
        for i in s:
            if i == "L":
                countL += 1
            if i == "R":
                countL -= 1
            if countL == 0:
                res += 1
        return res 
class Solution:
    def addDigits(self, num: int) -> int:
        count = 0
        while len(str(num)) > 1:
            for i in str(num):
                count = count + int(i)
                num = count
            count = 0
        return num
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i
        return n == 1
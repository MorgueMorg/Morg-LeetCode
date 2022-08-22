class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n & n - 1 == 0 and n % 10 in (1,4,6):
            return True
        return False
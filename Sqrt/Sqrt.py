class Solution:
    def mySqrt(self, x: int) -> int:
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2
        return int(result)
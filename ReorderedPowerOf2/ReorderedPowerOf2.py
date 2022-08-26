class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = len(str(n))
        c = sorted(str(n))
        for i in range((length-1) * 3 + length // 3, length * 3 + length // 3 + 1):
            if c == sorted(str(1 << i)):
                return True
        return False
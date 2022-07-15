class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        maxim = n // 2
        m = set(candyType)
        i = len(m)
        if i > maxim:
            return maxim
        else: return i


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
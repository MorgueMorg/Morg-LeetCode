class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        minimum = 0
        while (minutesToTest / minutesToDie + 1) ** minimum < buckets:
            minimum += 1
        return minimum


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets)/log(minutesToTest//minutesToDie + 1))
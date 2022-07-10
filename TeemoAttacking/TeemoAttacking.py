class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        var = 0
        for i in range(0, len(timeSeries) - 1):
            var += min(timeSeries[i + 1] - timeSeries[i], duration)
        return var + duration
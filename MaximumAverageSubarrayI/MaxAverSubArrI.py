class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        g = sum(nums[:k])
        m = g
        for i in range(len(nums) - k):
            g = g - nums[i] + nums[i + k]
            m = max(m, g)
        return m / k
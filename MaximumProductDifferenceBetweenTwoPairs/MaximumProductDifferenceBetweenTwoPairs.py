class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        w, x, y, z = nums[-1], nums[-2], nums[0], nums[1]
        return (w * x) - (y * z)
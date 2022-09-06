class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sort = sorted(nums)
        for i in range(len(sort) - 1):
            if max(nums) >= sort[i] * 2:
                continue
            else:
                return -1
        return nums.index(max(nums))
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        count = 1
        for i in nums:
            if i == count:
                count += 1
            elif i > 0:
                return count
        return count
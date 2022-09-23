class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total, rem  = 0, sum(nums)
        for i in range(len(nums)):
            total += nums[i]
            rem -= nums[i]
            if total > rem:
                return nums[:i + 1]
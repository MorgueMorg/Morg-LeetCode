class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        long, count = 0, 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                count, long = 1, max(long, count)
        return max(long, count)
    

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)
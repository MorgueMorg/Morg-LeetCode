class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k:
            nums.sort()
            nums[0] = - nums[0] 
            k = k - 1
        return sum(nums)
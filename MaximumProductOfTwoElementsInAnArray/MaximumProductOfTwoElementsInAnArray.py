class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        return (nums[0]-1)*(nums[1]-1)
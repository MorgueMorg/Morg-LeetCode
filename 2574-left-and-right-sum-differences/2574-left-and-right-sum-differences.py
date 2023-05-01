class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left, right = 0, sum(nums)
        for idx, val in enumerate(nums):
            left += val
            nums[idx] = abs(right - left)
            right -= val
        return nums
            
            
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        one, max_, two = 0, 0, len(nums) - 1
        while one <= two:
            max_ = max(max_, nums[one] + nums[two])
            one += 1
            two -= 1
        return max_
        
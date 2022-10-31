class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        one = 0
        two = len(nums) - 1
        max_ = 0
        while one <= two:
            max_ = max(max_, nums[one] + nums[two])
            one += 1
            two -= 1
        return max_
        
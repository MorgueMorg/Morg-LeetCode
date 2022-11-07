class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        for i, j in enumerate(nums):
            if i > max_:
                return False
            max_ = max(max_, i + j)
        return True
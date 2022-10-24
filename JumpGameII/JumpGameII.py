class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        farthest = 0
        end = 0
        for i in range(len(nums) - 1):
            cur = i + nums[i]
            farthest = max(farthest, cur)
            if i == end:
                end = farthest
                count += 1
        return count
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        index = 0
        for num in range(len(nums)):
            if num + 1 < len(nums) and nums[num] + 1 == nums[num + 1]:
                continue
            elif index == num:
                ranges.append(f"{nums[index]}")
            else:
                ranges.append(f"{nums[index]}->{nums[num]}")
            index = num + 1
        return ranges
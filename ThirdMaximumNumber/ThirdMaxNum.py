class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        el = sorted(set(nums))
        if len(el) == 3:
            return min(nums)
        elif len(el) < 3:
            return max(nums)
        else:
            return el[-3]
            
            

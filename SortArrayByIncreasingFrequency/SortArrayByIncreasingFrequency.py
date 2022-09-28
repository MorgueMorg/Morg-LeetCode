class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse = True)
        
        ans = sorted(nums, key = nums.count)
        
        return ans
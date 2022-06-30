# По классике бинарный поиск
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return right
    

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        prev_sum = l * (l + 1) // 2
        new_sum = sum(nums)
        return prev_sum - new_sum

    

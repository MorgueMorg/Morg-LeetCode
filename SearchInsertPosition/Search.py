class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
            nums.append(target)
            nums.sort()
            return nums.index(target)

# ! Бинарный поиск
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return left         
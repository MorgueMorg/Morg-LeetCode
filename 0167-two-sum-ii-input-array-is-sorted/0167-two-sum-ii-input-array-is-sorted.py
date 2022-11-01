class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if numbers[left] + numbers[i] == target:
                return [i + 1, left + 1]
        
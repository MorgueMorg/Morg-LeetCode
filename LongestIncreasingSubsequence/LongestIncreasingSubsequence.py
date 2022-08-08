class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left != right:
                middle = (left + right) // 2
                if tails[middle] < num:
                    left = middle + 1
                else:
                    right = middle
            tails[left] = num
            size = max(left + 1, size)
        return size
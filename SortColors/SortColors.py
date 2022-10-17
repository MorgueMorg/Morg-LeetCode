class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ! Пузырьковая сортировка, задача решается одной ф-ей sort()
        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Создаю переменную для элементов в массиве
        i = 1
        # Создаю цикл итераций
        while i < len(nums):
            # Сравнение элементов. Если элементы в списке одинаковы, элементы удаляются
            if nums[i-1] == nums[i]:nums.pop(i)
            # Либо инкрементирую элементы
            else:
                i += 1
            # Возвращаю длину мутированного массива как в условии
        return len(nums)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Переменная для проверки
        i = 0
        # Цикл для итераций
        while i < len(nums):
            # Условие, если i равно заданному значению val, то оно удаляется из списка
            if nums[i] == val: nums.pop(i)
            # Либо инкрементация элемента
            else: i += 1
        # По условию возвращаю длину мутированного списка
        return len(nums)
        
 # ! Один указатель
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

 # ! Сдвиги элементов
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Создаю переменную для сравнения
        i = 0
        # Цикл со второй перменной для сравнения с первой
        for j in range(1, len(nums)):
            # Если первая не равна второй, то 
            if nums[i] != nums[j]:
                # в таком случае передвигаю вперед первый элемент
                i += 1
                # Изменяю значения (ставлю в одно)
                nums[i] = nums[j]
        return i + 1
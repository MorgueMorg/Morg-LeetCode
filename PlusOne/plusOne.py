class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # По условию если в массиве один элемент и он не равен 9,то:
        if len(digits) == 1 and digits[0] == 9:
            # Возвращаю 1 и 0 по условию
            return [1, 0]
        # Если же последняя цифра массиве не 9, то присваиваю ей ее значение + 1
        if digits[-1] != 9:
            digits[-1] += 1
            # Возвращаю массив по условию
            return digits
        # Либо
        else:
            # Делаю последнюю цифру 0
            digits[-1] = 0
            # Прохожусь рекурсией
            digits[:-1] = self.plusOne(digits[:-1])
            # Возвращаю массив по условию
            return digits  


# ! Решение в одну строку с мапой
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
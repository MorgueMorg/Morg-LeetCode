class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Меняю строки на словари, чтобы после юзануть pop()
        a, b = list(a), list(b)
        # Переменная для переноса
        carry = 0
        # Переменная для среза
        ans = ""
        # Цикл для итераций
        while a or b or carry:
            # Приравниваю значение оборачивая в число
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            # Юзаю дивмод, который возвращает кортеж
            carry, remain = divmod(carry, 2)
            # Приравниваю к срезу по условию строку со значением
            ans += str(remain)
        # Возвращаю срез с отрицательным индексом, чтобы перевернуть результат
        return ans[::-1]


# ! Решение короче
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        totalNum = int(a,2) + int(b,2)
        return format(totalNum, "b")


# ! Решение в строку
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

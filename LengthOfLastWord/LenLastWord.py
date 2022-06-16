class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        # Цикл для итераций по строке, strip - убирает все пробелы в строке, i - буквы в строке
        for i in s.strip():
            # Если встречается пробел, длина будет 0
            if i == " ": length = 0
            # Иначе присваивается один пока не встретится пробел
            else: length += 1
        # Возвращаю длину строки до пробела (длину последнего слова)
        return length

class Solution:
    # Решение в строку
    def lengthOfLastWord(self, s: str) -> int:
        # Возвращаю длину строки без пробела по разделителю в отрицательном индексе
        # То есть длину последнего слова строки
        return len(s.rstrip().split(' ')[-1])
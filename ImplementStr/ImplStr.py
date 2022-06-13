class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # По условию если строка пустая возвращаю ноль
        if needle == "": return 0
        # Если элемент в строке, возвращаю индекс элемента
        if needle in haystack: return str.find(haystack, needle) 
        # Иначе по условию возвращаю -1
        return -1 

# -------------------------------------------------------------------------------------------------------------------#

# Более оптимизированный вариант
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Итерирую строку по длине
        for i in range(len(haystack) - len(needle) + 1):
            # Сравниваю подстроки
            if haystack[i:i+len(needle)] == needle:
                # Если needle существует в haystack возвращаю i
                return i
        # Либо по условию -1
        return -1
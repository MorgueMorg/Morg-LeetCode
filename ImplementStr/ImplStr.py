class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # По условию если строка пустая возвращаю ноль
        if needle == "":
            return 0
        # Если элемент в строке, возвращаю индекс элемента
        if needle in haystack:
            return str.find(haystack, needle) 
        # Иначе по условию возвращаю -1
        else: return -1 
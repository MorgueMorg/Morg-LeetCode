# Solution.isValid()
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # Создаю словарь для проверки (сходства) ключа и значения для разных скобок
        left_check_right = {'[': ']', '(': ')', '{': '}'}
        # Создаю лист, куда буду помещать скобки и сравнивать 
        arr = []
        # Создаю цикл для перебора элементов 
        for c in s:
            # Если элемент находится в словаре, то добавляю элемент в лист
            if c in left_check_right:
                arr.append(left_check_right[c])
            # Если лист равен нулю или не равен элементу, возвратить false 
            elif len(arr) == 0 or arr.pop() != c:
                return False
        return len(arr) == 0

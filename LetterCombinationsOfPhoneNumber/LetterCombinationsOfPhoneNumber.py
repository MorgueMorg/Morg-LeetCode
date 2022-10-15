class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        arr = []
        nums = {'2':"abc",
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz'
               }
        def helper(index, string):
            if index == len(digits):
                arr.append(string)
                return True
            # Цикл для проверки букв в каждой цифре (abc, def и т.д)
            for i in (nums[digits[index]]):
                string += i
                # + 1 потому что начинается с одной буквы a
                helper(index+1,string)
                string = string[:-1]
        helper(0, "")
        return arr
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1: return int(''.join(map(str, nums))) -> Эта строка необязательна, она делает из списка число
        x = 0
        for i in nums:
            # ^ -> Проводит побитовую операцию xor (исключающее или) на двух значениях. x = x ^ i
            x ^= i
        return x


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
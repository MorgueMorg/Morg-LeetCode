class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, mult = 0, 1 
        while n > 0:
            digit = n % 10
            sum_ = sum_ + digit
            mult = mult * digit
            n = n // 10
        return mult - sum_
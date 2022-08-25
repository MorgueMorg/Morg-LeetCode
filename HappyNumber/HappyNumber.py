class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()
        while n not in set_:
            set_.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1
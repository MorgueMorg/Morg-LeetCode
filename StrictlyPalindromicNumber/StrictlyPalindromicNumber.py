class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            arr = []
            num = n
            while num:
                arr.append(num % b)
                num = num // b
            if arr != arr[::-1]:
                return False
        return True
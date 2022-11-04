class Solution:
    def minOperations(self, n: int) -> int:
         return ((n + 1) // 2) * (n // 2)
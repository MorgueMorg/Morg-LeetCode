class Solution:
    # Тупо решаю тернарным оператором и рекурсией
    # Нельзя забывать прописывать self, из за ООП на самом сайте
    def fib(self, n: int) -> int:
        if n <= 1: return n
        return self.fib(n-1) + self.fib(n-2)

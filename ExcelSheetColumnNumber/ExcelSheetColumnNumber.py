"""
ORD() => Возвращает числовое представление для указанного символа.
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i, c in enumerate(reversed(columnTitle.upper())):
            res += (26 ** i) * (ord(c) - ord("A") + 1)
        return res  
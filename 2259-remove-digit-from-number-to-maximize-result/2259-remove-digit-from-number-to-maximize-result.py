class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        arr = []
        for i in range(len(number)):
            if number[i] == digit:
                arr.append(number[:i]+number[i+1:])
        return max(arr)
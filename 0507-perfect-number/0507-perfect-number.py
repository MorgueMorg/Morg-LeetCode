class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sums = 0
        if num == 1:
            return False
        
        for i in range(1, floor(num**0.5)+1):
            if num%i == 0:
                sums += i + num//i
        
        if sums == 2 * num:
            return True
        
        return False
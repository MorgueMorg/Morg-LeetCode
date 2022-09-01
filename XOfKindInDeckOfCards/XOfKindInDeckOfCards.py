class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hash = {}
        for num in deck:
            if num not in hash:
                hash[num] = 0
            hash[num] += 1
        
        countArr = list(hash.values())
        minCount = min(countArr)
        
        if minCount < 2: return False
        
        for i in range(2, minCount + 1):
            divisible = [a % i == 0 for a in countArr]
            if all(divisible):
                return True
        return False
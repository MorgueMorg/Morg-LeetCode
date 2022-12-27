class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [0] * len(capacity)
        res = 0
        
        for i in range(len(capacity)):
            remaining[i] = capacity[i] - rocks[i]
        remaining.sort()
        
        for i in range(len(remaining)):
            if remaining[i] > additionalRocks:
                break
                
            additionalRocks -= remaining[i]
            res += 1
        
        return res
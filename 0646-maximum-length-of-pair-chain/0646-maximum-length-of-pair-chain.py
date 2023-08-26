class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        count = 1  
        prev_elem = pairs[0]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > prev_elem[1]:
                count += 1
                prev_elem = pairs[i]
        
        return count
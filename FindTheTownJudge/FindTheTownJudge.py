class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0] * n
        trust_count = [0] * n
        
        for person in trust:
            arr[person[0] - 1] = 1
            trust_count[person[1] - 1] += 1
        
        for i in range(n):
            if arr[i]==0 and trust_count[i]==n-1: return i+1
        
        return -1
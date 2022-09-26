class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        raz = arr[1] - arr[0] 
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != raz:
                return False
            
        return True
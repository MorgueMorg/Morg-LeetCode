class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        x = int(0.05*len(arr))
        arr = arr[x:]
        arr = arr[:-x]
        return sum(arr)/len(arr)
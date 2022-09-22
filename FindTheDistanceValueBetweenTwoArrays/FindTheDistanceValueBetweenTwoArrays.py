class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        set_ = set()
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    set_.add(i)
        return len(arr1) - len(set_)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in arr2:
            for j in range(arr1.count(i)):
                l1.append(i)
        for x in arr1:
            if x not in l1:
                l2.append(x)
        l2.sort()
        return l1 + l2  
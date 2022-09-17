class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dct = {}
        for i in arr:
            if i / 2 in dct or i * 2 in dct:
                return True
            else:
                dct[i] = 1
        return False
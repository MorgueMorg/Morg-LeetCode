class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dct = {}
        for i in arr:
            if i / 2 in dct or i * 2 in dct:
                return True
            else:
                dct[i] = 1
        return False


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i * 2 in arr and i != 0:
                return True
            elif i == 0 and (arr.count(i) > 1):
                return True
        return False
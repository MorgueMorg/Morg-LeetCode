class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target == arr:
            return True
        return False


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in target:
            if (i not in arr) or (arr.count(i) != target.count(i)):
                return False
        return True
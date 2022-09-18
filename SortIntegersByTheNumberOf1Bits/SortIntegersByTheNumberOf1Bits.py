class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr_list = []
        for a in arr:
            arr_list.append((bin(a).count('1'), a))
        arr_list.sort()
        return [k[1] for k in arr_list]
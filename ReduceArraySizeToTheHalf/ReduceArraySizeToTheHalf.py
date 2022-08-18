class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict_ = {}
        for i in arr:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        list_ = sorted(dict_.values())
        length = len(arr) // 2
        res = 0
        while length > 0:
            length -= list_[-res-1]
            res += 1
        return res

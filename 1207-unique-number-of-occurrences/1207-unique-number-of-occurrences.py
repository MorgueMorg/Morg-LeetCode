class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = dict()
        for i in arr:
            dict_[i] = arr.count(i)
        return len(dict_.values()) == len(set(dict_.values()))